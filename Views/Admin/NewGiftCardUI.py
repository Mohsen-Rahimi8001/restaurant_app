from PyQt5 import QtCore, QtGui, QtWidgets
from Window import Routing
from Controllers.AuthenticationController import Auth
from Lib.Questions import Questions
from Lib.Messages import Messages
from Models.GiftCard import GiftCard
import datetime as dt



def checkForCredentials(window: "QtWidgets.QMainWindow"):
    """Checks if the user is logged in and has the admin credentials."""
    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'main')
        Routing.ClearStack()


# ////////////////////////////////EVENTS////////////////////////////
def clearPage(ui: "Ui_MainWindow"):
    """Clears the form."""
    
    # set the code to empty
    ui.lEditCode.setText("")
    # set the slider to zero
    ui.hSliderAmount.setValue(0)
    # set the start date to today
    ui.calendarStartDate.setSelectedDate(QtCore.QDate.currentDate())   
    # set the expiration date to today
    ui.calendarExpirationDate.setSelectedDate(QtCore.QDate.currentDate())


def addGiftCard(ui: "Ui_MainWindow"):
    """Adds a giftcard to the database."""

    # get the code
    code = ui.lEditCode.text()
    # get the amount
    amount = ui.hSliderAmount.value()
    # get the start date
    start_date = ui.calendarStartDate.selectedDate()

    # convert the date to the write format
    start_date = dt.datetime(start_date.year(), start_date.month(), start_date.day()).strftime('%Y-%m-%d')

    # get the expiration date
    expiration_date = ui.calendarExpirationDate.selectedDate()

    # convert the date to the write format
    expiration_date = dt.datetime(expiration_date.year(), expiration_date.month(), expiration_date.day()).strftime('%Y-%m-%d')

    # check if the necessary data is entered
    if code == "":
        if not Questions.ask(Questions.Type.ASKOKCANCEL, "You didn't enter the code. \nDo you want to set a random code?"):
            return
    
    try:    
        # create the giftcard
        GiftCard.Create({
            'start_date': start_date,
            'expiration_date': expiration_date,
            'amount': amount,
            'code': code
        })

    except Exception as e:
        Messages.push(Messages.Type.ERROR, str(e))
        Messages.show()
        return
    
    else:
        # show a message
        Messages.push(Messages.Type.SUCCESS, "Giftcard added successfully.")
        Messages.show()

        # clear the form
        clearPage(ui)


def showSlider(ui: "Ui_MainWindow", value):
    """Shows the value of the slider."""
    ui.lblShowAmount.setText(str(value))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 986, 680))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.lEditCode = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditCode.setObjectName("lEditCode")
        self.gridLayout.addWidget(self.lEditCode, 1, 1, 1, 2)
        self.lblExpirationDate = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblExpirationDate.setFont(font)
        self.lblExpirationDate.setObjectName("lblExpirationDate")
        self.gridLayout.addWidget(self.lblExpirationDate, 4, 0, 1, 1)
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setSpacing(20)
        self.btnHLayout.setObjectName("btnHLayout")
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda:Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(lambda:clearPage(self))
        self.btnHLayout.addWidget(self.btnClear)
        
        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(lambda:addGiftCard(self))
        self.btnHLayout.addWidget(self.btnAdd)
        self.gridLayout.addLayout(self.btnHLayout, 5, 0, 1, 3)
        self.lblStartDate = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblStartDate.setFont(font)
        self.lblStartDate.setObjectName("lblStartDate")
        self.gridLayout.addWidget(self.lblStartDate, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 3)

        self.hSliderAmount = QtWidgets.QSlider(self.gridLayoutWidget)
        self.hSliderAmount.setOrientation(QtCore.Qt.Horizontal)
        self.hSliderAmount.setObjectName("hSliderAmount")
        self.hSliderAmount.valueChanged.connect(lambda value :showSlider(self, value))
        self.gridLayout.addWidget(self.hSliderAmount, 2, 1, 1, 1)

        self.lblShowAmount = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblShowAmount.setFont(font)
        self.lblShowAmount.setObjectName("lblNewAmount")
        self.gridLayout.addWidget(self.lblShowAmount, 2, 2, 1, 1)

        self.lblCode = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblCode.setFont(font)
        self.lblCode.setObjectName("lblCode")
        self.gridLayout.addWidget(self.lblCode, 1, 0, 1, 1)
        self.lblAmount = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblAmount.setFont(font)
        self.lblAmount.setObjectName("lblAmount")
        self.gridLayout.addWidget(self.lblAmount, 2, 0, 1, 1)
        self.calendarStartDate = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarStartDate.setObjectName("calendarStartDate")
        self.gridLayout.addWidget(self.calendarStartDate, 3, 1, 1, 2)
        self.calendarExpirationDate = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        self.calendarExpirationDate.setObjectName("calendarExpirationDate")
        self.gridLayout.addWidget(self.calendarExpirationDate, 4, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblExpirationDate.setText(_translate("MainWindow", "Expiration Date: "))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.lblStartDate.setText(_translate("MainWindow", "Start Date: "))
        self.lblTitle.setText(_translate("MainWindow", "New Gift Card"))
        self.lblCode.setText(_translate("MainWindow", "Code: "))
        self.lblAmount.setText(_translate("MainWindow", "Amount: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
