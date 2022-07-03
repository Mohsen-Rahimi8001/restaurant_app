from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Restaurant import Restaurant
from Controllers.AuthenticationController import Auth
from Window import Routing
from Lib.Messages import Messages
from Lib.Questions import Questions


def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """checks if the user is admin"""

    if not Auth.CheckAdminCredentials():
        # Logout the user
        Auth.Logout()
        # Go to the login window
        Routing.Redirect(window, "landingPage")
        Routing.ClearStack() # prevent the user from going back to the previous window


# /////////////////////////////EVENTS////////////////////////////

def setUpInitialInformation(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """Fill Restaurant information in the page"""
    
    restaurant = Restaurant.LoadFromJson()

    ui.lEditRestName.setText(restaurant.restaurantName)
    ui.lEditManName.setText(restaurant.managerName)
    ui.lEditManEmail.setText(restaurant.managerEmail)
    ui.lEditType.setText(restaurant.type)
    ui.lEditPhone.setText(restaurant.phone)
    ui.lEditAddress.setText(restaurant.address)
    ui.lEditRegion.setText(restaurant.region)
    ui.lEditDescription.setText(restaurant.description)


def clearPage(ui: "Ui_MainWindow"):
    """Clear the page"""

    ui.lEditRestName.setText("")
    ui.lEditManName.setText("")
    ui.lEditManEmail.setText("")
    ui.lEditType.setText("")
    ui.lEditPhone.setText("")
    ui.lEditAddress.setText("")
    ui.lEditRegion.setText("")
    ui.lEditDescription.setText("")


def refreshPage(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """Refresh the page"""

    clearPage(ui)
    setUpInitialInformation(ui, window)


def saveChanges(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """save the changes"""

    # check if all the information is entered
    if not ui.lEditRestName.text() or not ui.lEditManName.text() or not ui.lEditManEmail.text()\
         or not ui.lEditType.text() or not ui.lEditPhone.text() or not ui.lEditAddress.text()\
             or not ui.lEditRegion.text() or not ui.lEditDescription.text():
             Messages.push(Messages.Type.ERROR, "Please fill all the information")
             Messages.show()
             return

    # # check if the phone number is an integer
    # if not ui.lEditPhone.text().isdigit():
    #     Messages.push(Messages.Type.ERROR, "Phone number must be a number")

    try:
        restaurant = Restaurant(
            restaurantName=ui.lEditRestName.text(),
            managerName=ui.lEditManName.text(),
            managerEmail=ui.lEditManEmail.text(),
            type=ui.lEditType.text(),
            description=ui.lEditDescription.text(),
            phone=ui.lEditPhone.text(),
            region=ui.lEditRegion.text(),
            address=ui.lEditAddress.text(),
        )
    except Exception as e:
        Messages.push(Messages.Type.ERROR, str(e))
        Messages.show()
        return
    else:
        restaurant.SaveToJson()
        Messages.push(Messages.Type.SUCCESS, "Changes saved successfully")
        Messages.show()
        refreshPage(ui, window)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 771, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)

        self.lblRestName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRestName.setFont(font)
        self.lblRestName.setObjectName("lblRestName")
        self.gridLayout.addWidget(self.lblRestName, 1, 0, 1, 1)

        self.lEditRestName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditRestName.setClearButtonEnabled(True)
        self.lEditRestName.setObjectName("lEditRestName")
        self.gridLayout.addWidget(self.lEditRestName, 1, 1, 1, 1)

        self.lblManName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblManName.setFont(font)
        self.lblManName.setObjectName("lblManName")
        self.gridLayout.addWidget(self.lblManName, 2, 0, 1, 1)
        
        self.lEditManName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditManName.setClearButtonEnabled(True)
        self.lEditManName.setObjectName("lEditManName")
        self.gridLayout.addWidget(self.lEditManName, 2, 1, 1, 1)

        self.lblManEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblManEmail.setFont(font)
        self.lblManEmail.setObjectName("lblManEmail")
        self.gridLayout.addWidget(self.lblManEmail, 3, 0, 1, 1)

        self.lEditManEmail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditManEmail.setClearButtonEnabled(True)
        self.lEditManEmail.setObjectName("lEditManEmail")
        self.gridLayout.addWidget(self.lEditManEmail, 3, 1, 1, 1)

        self.lblType = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblType.setFont(font)
        self.lblType.setObjectName("lblType")
        self.gridLayout.addWidget(self.lblType, 4, 0, 1, 1)

        self.lEditType = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditType.setClearButtonEnabled(True)
        self.lEditType.setObjectName("lEditType")
        self.gridLayout.addWidget(self.lEditType, 4, 1, 1, 1)

        self.lblDescription = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblDescription.setFont(font)
        self.lblDescription.setObjectName("lblDescription")
        self.gridLayout.addWidget(self.lblDescription, 5, 0, 1, 1)

        self.lEditDescription = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditDescription.setClearButtonEnabled(True)
        self.lEditDescription.setObjectName("lEditDescription")
        self.gridLayout.addWidget(self.lEditDescription, 5, 1, 1, 1)

        self.lblPhone = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblPhone.setFont(font)
        self.lblPhone.setObjectName("lblPhone")
        self.gridLayout.addWidget(self.lblPhone, 6, 0, 1, 1)
        
        self.lEditPhone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditPhone.setClearButtonEnabled(True)
        self.lEditPhone.setObjectName("lEditPhone")
        self.gridLayout.addWidget(self.lEditPhone, 6, 1, 1, 1)

        self.lblRegion = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRegion.setFont(font)
        self.lblRegion.setObjectName("lblRegion")
        self.gridLayout.addWidget(self.lblRegion, 7, 0, 1, 1)
        
        self.lEditRegion = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditRegion.setClearButtonEnabled(True)
        self.lEditRegion.setObjectName("lEditRegion")
        self.gridLayout.addWidget(self.lEditRegion, 7, 1, 1, 1)

        self.lblAddress = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblAddress.setFont(font)
        self.lblAddress.setObjectName("lblAddress")
        self.gridLayout.addWidget(self.lblAddress, 8, 0, 1, 1)

        self.lEditAddress = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditAddress.setClearButtonEnabled(True)
        self.lEditAddress.setObjectName("lEditAddress")
        self.gridLayout.addWidget(self.lEditAddress, 8, 1, 1, 1)
        
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setContentsMargins(5, 5, 5, 5)
        self.btnHLayout.setSpacing(20)
        self.btnHLayout.setObjectName("horizontalLayout")
        
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
        
        self.btnRefresh = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.clicked.connect(lambda:refreshPage(self, MainWindow))
        self.btnHLayout.addWidget(self.btnRefresh)
        
        self.btnChange = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnChange.setFont(font)
        self.btnChange.setObjectName("btnChange")
        self.btnChange.clicked.connect(lambda:saveChanges(self, MainWindow))
        self.btnHLayout.addWidget(self.btnChange)
        self.gridLayout.addLayout(self.btnHLayout, 9, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblManName.setText(_translate("MainWindow", "New Manager Name: "))
        self.lblRegion.setText(_translate("MainWindow", "New Region: "))
        self.lEditRestName.setPlaceholderText(_translate("MainWindow", "New Restaurant Name"))
        self.lEditManName.setPlaceholderText(_translate("MainWindow", "New Manager Name"))
        self.lblManEmail.setText(_translate("MainWindow", "New Email: "))
        self.lEditAddress.setPlaceholderText(_translate("MainWindow", "New Address"))
        self.lEditDescription.setPlaceholderText(_translate("MainWindow", "New Description"))
        self.lblPhone.setText(_translate("MainWindow", "New Phone: "))
        self.lEditManEmail.setPlaceholderText(_translate("MainWindow", "New Email"))
        self.lblDescription.setText(_translate("MainWindow", "New Description: "))
        self.lblType.setText(_translate("MainWindow", "New Type: "))
        self.lblTitle.setText(_translate("MainWindow", "Edit Restaurant Info"))
        self.lEditPhone.setPlaceholderText(_translate("MainWindow", "New Phone Number"))
        self.lblRestName.setText(_translate("MainWindow", "New Restaurant Name: "))
        self.lEditRegion.setPlaceholderText(_translate("MainWindow", "New Region"))
        self.lblAddress.setText(_translate("MainWindow", "New Address: "))
        self.lEditType.setPlaceholderText(_translate("MainWindow", "New Type"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnRefresh.setText(_translate("MainWindow", "Retrieve Information"))
        self.btnChange.setText(_translate("MainWindow", "Change"))

        # check if the user is admin
        checkForCredentials(MainWindow)

        setUpInitialInformation(self, MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
