from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Window import Routing
from Models.Order import Order
from Lib.Messages import Messages
from functools import partial


def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """Checks if the user is logged in and has the admin credentials."""
    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'main')
        Routing.ClearStack()


def setUpInitInformation(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """fetches all the orders and fills them in the table"""               

    # get all the orders
    orders = Order.GetAll()

    index = -1

    for order in orders:

        index += 1

        if order.confirmed:
            index -= 1
            continue

        # increase row count by one
        ui.tableOrders.setRowCount(ui.tableOrders.rowCount() + 1)

        # create a accept button
        acceptIcon = QtGui.QIcon(r".\Resources\Images\accept_icon.png")
        btnAccept = QtWidgets.QPushButton()
        btnAccept.setIcon(acceptIcon)
        btnAccept.setIconSize(QtCore.QSize(20, 20))
        acceptSignal = partial(acceptOrder, order.id, window)

        # create a show button
        showIcon = QtGui.QIcon(r".\Resources\Images\show_icon.png")
        btnShow = QtWidgets.QPushButton()
        btnShow.setIcon(showIcon)
        btnShow.setIconSize(QtCore.QSize(20, 20))
        showSignal = partial(showOrder, order.id)

        ui.tableOrders.setItem(index, 0, QtWidgets.QTableWidgetItem(str(order.id)))

        foods = ""
        for food in order.getFoods():
            foods += f"{food.title}, "

        ui.tableOrders.setItem(index, 1, QtWidgets.QTableWidgetItem(foods.rstrip(", ")))
        ui.tableOrders.setItem(index, 2, QtWidgets.QTableWidgetItem(str(order.order_date)))

        if order.payment_method == 0:
            ui.tableOrders.setItem(index, 3, QtWidgets.QTableWidgetItem("Online"))
        elif order.payment_method == 1:
            ui.tableOrders.setItem(index, 3, QtWidgets.QTableWidgetItem("Cash"))

        ui.tableOrders.setItem(index, 4, QtWidgets.QTableWidgetItem(str(order.reference_number)))
        ui.tableOrders.setItem(index, 5, QtWidgets.QTableWidgetItem(str(order.account_number)))

        # add the accept buttons to the table
        ui.tableOrders.setCellWidget(index, 6, btnAccept)

        # add the show buttons to the table
        ui.tableOrders.setCellWidget(index, 7, btnShow)

        # connect the signals
        btnAccept.clicked.connect(acceptSignal)
        btnShow.clicked.connect(showSignal)

        
# ////////////////////////////EVENTS////////////////////////////
def acceptOrder(orderId: int, window: 'QtWidgets.QMainWindow'):
    """Accept the order and confirm it"""

    # get the order
    order = Order.Get(orderId)

    # confirm the order
    order.confirm()

    # show a message
    Messages.push(Messages.Type.SUCCESS, "Order confirmed")

    # refresh the table
    Routing.Refresh(window)



def showOrder(orderId: int):
    """Show the order information in an info message"""

    # get the order
    order = Order.Get(orderId)

    totalInterest = 0

    # foods information
    foods = ""

    # calculate the total interest
    for i, food in enumerate(order.getFoods()):
        totalInterest += food.sale_price - food.fixed_price
        foods += f"Food {i}) Title: {food.title}, Stock: {food.stock}, Interest: {food.sale_price - food.fixed_price}\n"

    # show the order
    message = f"Foods:\n{foods}\n________________________________________________\nTotal Interest: {totalInterest}"

    # show the message
    Messages.push(Messages.Type.INFO, message)
    Messages.show()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1201, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)
        
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda:Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        
        self.btnRefersh = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnRefersh.setFont(font)
        self.btnRefersh.setObjectName("btnRefersh")
        self.btnRefersh.clicked.connect(lambda:Routing.Refresh(MainWindow))
        self.btnHLayout.addWidget(self.btnRefersh)
        
        self.gridLayout.addLayout(self.btnHLayout, 2, 0, 1, 1)
        
        self.tableOrders = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableOrders.setObjectName("tableOrders")
        self.tableOrders.setColumnCount(8)
        self.tableOrders.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(6, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableOrders.setHorizontalHeaderItem(7, item)
        
        self.tableOrders.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.gridLayout.addWidget(self.tableOrders, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Orders"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnRefersh.setText(_translate("MainWindow", "Refresh"))
        item = self.tableOrders.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableOrders.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Foods"))
        item = self.tableOrders.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableOrders.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Payment Method"))
        item = self.tableOrders.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Refrence Number"))
        item = self.tableOrders.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "User Account"))
        item = self.tableOrders.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Accept"))
        item = self.tableOrders.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Show"))

        checkForCredentials(MainWindow)
        setUpInitInformation(self, MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
