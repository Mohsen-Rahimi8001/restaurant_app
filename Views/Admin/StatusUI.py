from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Window import Routing
from Models.Restaurant import Restaurant



def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """Checks if the user is logged in and has the admin credentials."""

    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'main')
        Routing.ClearStack()


def setUpTable(ui: 'Ui_MainWindow'):
    """Fetches all the economic information and sets it to the table."""
    
    data = Restaurant.GetRestaurantEconomy()

    ui.tableRecords.setRowCount(len(data) - 1)

    total_sale = data.pop("total")
    total_interest = data.pop('total_interest')
    
    ui.tableRecords.setItem(0, 0, QtWidgets.QTableWidgetItem("Total"))
    ui.tableRecords.setItem(0, 1, QtWidgets.QTableWidgetItem(str(total_interest)))
    ui.tableRecords.setItem(0, 2, QtWidgets.QTableWidgetItem(str(total_sale)))
    
    for i, date in enumerate(data, start=1):
        
        ui.tableRecords.setItem(i, 0, QtWidgets.QTableWidgetItem(date))
        ui.tableRecords.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[date][1])))
        ui.tableRecords.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[date][0])))
        


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 681, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda: Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        self.gridLayout.addLayout(self.btnHLayout, 2, 0, 1, 1)
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
        self.tableRecords = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableRecords.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableRecords.setObjectName("tableRecords")
        self.tableRecords.setColumnCount(3)
        self.tableRecords.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecords.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecords.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRecords.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableRecords, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.lblTitle.setText(_translate("MainWindow", "Restaurant Economics"))
        item = self.tableRecords.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableRecords.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Total Interest"))
        item = self.tableRecords.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total Sale"))

        checkForCredentials(MainWindow)
        setUpTable(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
