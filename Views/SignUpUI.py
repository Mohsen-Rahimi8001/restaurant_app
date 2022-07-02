from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Lib.Messages import Messages
from Window import Routing
from Models.User import User
from functools import partial
#
# #////////////////////////////EVENTS///////////////////////////
from Controllers.AuthenticationController import Auth

def submit(window, ui : "Ui_MainWindow"):

    data = \
    {
        "first_name" : getFirstName(ui),
        "last_name" : getLastName(ui),
        "email" : getEmail(ui),
        "phone_number" : getPhoneNumber(ui),
        "social_number" : getSocialNumber(ui),
        "password" : getPassword(ui),
        "password_verification" : getPasswordVerification(ui)
    }

    result = Auth.SignUp(data)

    if result:
        Messages.push(Messages.Type.SUCCESS, "sign up completed")
        Routing.Redirect(window, "main")
        print(User.GetAll())
    else:
        Messages.push(Messages.Type.INFO, "sign up failed")
        Routing.Refresh(window)




#get inputs

def getFirstName(ui : "Ui_MainWindow"):
    return ui.lEditName.text().strip()

def getLastName(ui : "Ui_MainWindow"):
    return ui.lEditFamily.text().strip()

def getPhoneNumber(ui : "Ui_MainWindow"):
    return ui.lEditPhoneNumber.text().strip()

def getEmail(ui : "Ui_MainWindow"):
    return ui.lEditEmail.text().strip()

def getSocialNumber(ui : "Ui_MainWindow"):
    return ui.lEditSocialNumber.text().strip()

def getPassword(ui : "Ui_MainWindow"):
    return ui.lEditPassword.text().strip()

def getPasswordVerification(ui : "Ui_MainWindow"):
    return ui.lEditPasswordVerify.text().strip()



#//////////////////////////////UI//////////////////////////////

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 731, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        self.lEditName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditName.setAutoFillBackground(False)
        self.lEditName.setClearButtonEnabled(True)
        self.lEditName.setObjectName("lEditName")
        self.gridLayout.addWidget(self.lEditName, 1, 1, 1, 1)

        self.lblPassword = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.gridLayout.addWidget(self.lblPassword, 6, 0, 1, 1)
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)

        self.lEditFamily = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditFamily.setClearButtonEnabled(True)
        self.lEditFamily.setObjectName("lEditFamily")
        self.gridLayout.addWidget(self.lEditFamily, 2, 1, 1, 1)

        self.lblEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout.addWidget(self.lblEmail, 4, 0, 1, 1)

        self.lEditPassword = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lEditPassword.setClearButtonEnabled(True)
        self.lEditPassword.setObjectName("lEditPassword")
        self.gridLayout.addWidget(self.lEditPassword, 6, 1, 1, 1)

        self.lEditPhoneNumber = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditPhoneNumber.setClearButtonEnabled(True)
        self.lEditPhoneNumber.setObjectName("lEditPhoneNumber")
        self.gridLayout.addWidget(self.lEditPhoneNumber, 3, 1, 1, 1)
        self.lblPhoneNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblPhoneNumber.setFont(font)
        self.lblPhoneNumber.setObjectName("lblPhoneNumber")
        self.gridLayout.addWidget(self.lblPhoneNumber, 3, 0, 1, 1)

        self.lblPassVerification = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblPassVerification.setFont(font)
        self.lblPassVerification.setObjectName("lblPassVerification")
        self.gridLayout.addWidget(self.lblPassVerification, 7, 0, 1, 1)

        self.lEditSocialNumber = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditSocialNumber.setClearButtonEnabled(True)
        self.lEditSocialNumber.setObjectName("lEditSocialNumber")

        self.gridLayout.addWidget(self.lEditSocialNumber, 5, 1, 1, 1)
        self.lEditEmail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditEmail.setClearButtonEnabled(True)
        self.lEditEmail.setObjectName("lEditEmail")
        self.gridLayout.addWidget(self.lEditEmail, 4, 1, 1, 1)

        self.lblName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 1, 0, 1, 1)

        self.lblFamily = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblFamily.setFont(font)
        self.lblFamily.setObjectName("lblFamily")
        self.gridLayout.addWidget(self.lblFamily, 2, 0, 1, 1)

        self.lblSocialNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblSocialNumber.setFont(font)
        self.lblSocialNumber.setObjectName("lblSocialNumber")
        self.gridLayout.addWidget(self.lblSocialNumber, 5, 0, 1, 1)

        self.lEditPasswordVerify = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditPasswordVerify.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lEditPasswordVerify.setClearButtonEnabled(True)
        self.lEditPasswordVerify.setObjectName("lEditPasswordVerify")



        self.gridLayout.addWidget(self.lEditPasswordVerify, 7, 1, 1, 1)
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setSpacing(20)
        self.btnHLayout.setObjectName("btnHLayout")
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnHLayout.addWidget(self.btnClear)
        self.btnSubmit = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")

        bound_signup = partial(submit, MainWindow, self)
        self.btnSubmit.clicked.connect(bound_signup)


        self.btnHLayout.addWidget(self.btnSubmit)
        self.gridLayout.addLayout(self.btnHLayout, 8, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lEditName.setPlaceholderText(_translate("MainWindow", "Enter your first name"))
        self.lblPassword.setText(_translate("MainWindow", "Password: "))
        self.lblTitle.setText(_translate("MainWindow", "SignUp page"))
        self.lEditFamily.setPlaceholderText(_translate("MainWindow", "Enter your last name "))
        self.lblEmail.setText(_translate("MainWindow", "Email: "))
        self.lEditPassword.setPlaceholderText(_translate("MainWindow", "At least 8 chars consist of lower case and upper case letters and numbers and symbols"))
        self.lEditPhoneNumber.setPlaceholderText(_translate("MainWindow", "Valid forms (<00989|+9809|9|09>*********)"))
        self.lblPhoneNumber.setText(_translate("MainWindow", "Phone number: "))
        self.lblPassVerification.setText(_translate("MainWindow", "Password verification: "))
        self.lEditSocialNumber.setPlaceholderText(_translate("MainWindow", "Example: 0123456789"))
        self.lEditEmail.setPlaceholderText(_translate("MainWindow", "Example:  foo@bar.com"))
        self.lblName.setText(_translate("MainWindow", "Name: "))
        self.lblFamily.setText(_translate("MainWindow", "Family: "))
        self.lblSocialNumber.setText(_translate("MainWindow", "Social number: "))
        self.lEditPasswordVerify.setPlaceholderText(_translate("MainWindow", "Repeat your password"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
