from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Window import Routing
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Lib.Questions import Questions
from Lib.Image import Image
from Models.Restaurant import Restaurant
from Controllers.User.UserInfoController import UserInfo



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):
        user = Auth.GetUser()

        setFirstName(ui, user.first_name)
        setLastName(ui, user.last_name)
        setPhoneNumber(ui, user.phone_number)
        setSocialNumber(ui, user.social_number)
        setEmail(ui, user.email)
        setImageShowPixmap(ui, user.image)



def logout(window : QtWidgets.QMainWindow):

        questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
        if questionResult:
                Auth.LogOut()
                Routing.ClearStack()
                Routing.Redirect(window, "login")


def submit(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

        data = {
                "first_name" : getFirstName(ui),
                "last_name" : getLastName(ui),
                "phone_number" : getPhoneNumber(ui),
                "social_number" : getSocialNumber(ui),
                "email" : getEmail(ui),
                "password" : getPassword(ui),
                "new_password" : getNewPassword(ui),
                "image" : getImagePath(ui),
        }

        UserInfo.Edit(data)
        Routing.Refresh(window)


def browse(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

        path = Image.Browse(window)

        if path:
                setImageShowPixmap(ui, path)
                setImagePath(ui, path)


# get input methods

def getFirstName(ui : "Ui_MainWindow"):
        return ui.firstNameEdit.text().strip()

def getLastName(ui : "Ui_MainWindow"):
        return ui.lastNameEdit.text().strip()

def getPhoneNumber(ui : "Ui_MainWindow"):
        return ui.phoneNumberEdit.text().strip()

def getSocialNumber(ui : "Ui_MainWindow"):
        return ui.socialNumberEdit.text().strip()

def getPassword(ui : "Ui_MainWindow"):
        return ui.passwordEdit.text().strip()

def getNewPassword(ui : "Ui_MainWindow"):
        return ui.newPasswordEdit.text().strip()

def getEmail(ui : "Ui_MainWindow"):
        return ui.emaiEdit.text().strip()

def getImagePath(ui : "Ui_MainWindow"):
        return ui.imageEdit.text().strip()


#set methods

def setFirstName(ui : "Ui_MainWindow", value : str):
        ui.firstNameEdit.setText(str(value))

def setLastName(ui : "Ui_MainWindow", value : str):
        ui.lastNameEdit.setText(str(value))

def setPhoneNumber(ui : "Ui_MainWindow", value : str):
        ui.phoneNumberEdit.setText(str(value))

def setSocialNumber(ui : "Ui_MainWindow", value : str):
        ui.socialNumberEdit.setText(str(value))

def setPassword(ui : "Ui_MainWindow", value : str):
        ui.passwordEdit.setText(str(value))

def setNewPassword(ui : "Ui_MainWindow", value : str):
        ui.newPasswordEdit.setText(str(value))

def setEmail(ui : "Ui_MainWindow", value : str):
        ui.emaiEdit.setText(str(value))

def setImagePath(ui : "Ui_MainWindow", value : str):
        ui.imageEdit.setText(str(value))

def setImageShowPixmap(ui : "Ui_MainWindow", path : str):
        ui.imageShowLabel.setPixmap(QtGui.QPixmap(path))
        ui.imageShowLabel.setScaledContents(True)

#////////////////////////////UI/////////////////////////////



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(225, 230, 239);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(850, 110, 91, 50))
        self.orderBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"font-weight : 500;\n"
"font-size: 10pt;\n"
"color : rgb(49, 165, 25);")
        self.orderBtn.setObjectName("orderBtn")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 90, 841, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("border-color: rgb(4, 84, 83);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style : solid;\n"
"border-width : 1px;\n"
"border-right-width : 0px;\n"
"border-bottom-width : 0px;\n"
"border-top-left-radius : 20px;\n"
"border-bottom-right-radius: 0px;\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imageShowLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageShowLabel.setGeometry(QtCore.QRect(50, 50, 181, 131))
        self.imageShowLabel.setStyleSheet("border-width : 0px;\n"
"border-radius:0px;")
        self.imageShowLabel.setText("")
        self.imageShowLabel.setObjectName("imageShowLabel")
        self.firstNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.firstNameLabel.setGeometry(QtCore.QRect(50, 230, 101, 31))
        self.firstNameLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstNameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.firstNameEdit.setGeometry(QtCore.QRect(150, 230, 231, 31))
        self.firstNameEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.firstNameEdit.setObjectName("firstNameEdit")
        self.lastNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lastNameLabel.setGeometry(QtCore.QRect(410, 230, 101, 31))
        self.lastNameLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastNameEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lastNameEdit.setGeometry(QtCore.QRect(510, 230, 231, 31))
        self.lastNameEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.lastNameEdit.setObjectName("lastNameEdit")
        self.phoneNumberLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.phoneNumberLabel.setGeometry(QtCore.QRect(50, 280, 101, 31))
        self.phoneNumberLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")
        self.socialNumberLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.socialNumberLabel.setGeometry(QtCore.QRect(410, 280, 101, 31))
        self.socialNumberLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.socialNumberLabel.setObjectName("socialNumberLabel")
        self.socialNumberEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.socialNumberEdit.setGeometry(QtCore.QRect(510, 280, 231, 31))
        self.socialNumberEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.socialNumberEdit.setObjectName("socialNumberEdit")
        self.phoneNumberEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.phoneNumberEdit.setGeometry(QtCore.QRect(150, 280, 231, 31))
        self.phoneNumberEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.phoneNumberEdit.setObjectName("phoneNumberEdit")
        self.emailLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.emailLabel.setGeometry(QtCore.QRect(50, 380, 101, 31))
        self.emailLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.emailLabel.setObjectName("emailLabel")
        self.newPasswordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.newPasswordLabel.setGeometry(QtCore.QRect(410, 330, 101, 31))
        self.newPasswordLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.newPasswordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.newPasswordEdit.setGeometry(QtCore.QRect(510, 330, 231, 31))
        self.newPasswordEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.emaiEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.emaiEdit.setGeometry(QtCore.QRect(150, 380, 231, 31))
        self.emaiEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.emaiEdit.setObjectName("emaiEdit")
        self.passwordLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.passwordLabel.setGeometry(QtCore.QRect(50, 330, 101, 31))
        self.passwordLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.passwordLabel.setObjectName("passwordLabel")
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setGeometry(QtCore.QRect(50, 430, 101, 31))
        self.imageLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.imageLabel.setObjectName("imageLabel")
        self.imageEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.imageEdit.setGeometry(QtCore.QRect(150, 430, 361, 31))
        self.imageEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.imageEdit.setObjectName("imageEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.passwordEdit.setGeometry(QtCore.QRect(150, 330, 231, 31))
        self.passwordEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.passwordEdit.setObjectName("passwordEdit")
        self.browseBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.browseBtn.setGeometry(QtCore.QRect(510, 430, 101, 31))
        self.browseBtn.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.browseBtn.setObjectName("browseBtn")
        self.submitBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.submitBtn.setGeometry(QtCore.QRect(50, 490, 121, 41))
        self.submitBtn.setStyleSheet("border-width:0px;\n"
"color: rgb(4, 85, 80);\n"
"background-color: rgb(52, 163, 21, 100);\n"
"border-bottom-width : 0px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"font-weight : 500;\n"
"font-size: 9pt;\n"
"\n"
"\n"
"")
        self.submitBtn.setObjectName("submitBtn")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.historyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.historyBtn.setGeometry(QtCore.QRect(850, 230, 91, 50))
        self.historyBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(49, 165, 25);\n"
"font-weight : 500;\n"
"font-size: 9pt;")
        self.historyBtn.setObjectName("historyBtn")
        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setGeometry(QtCore.QRect(850, 350, 91, 50))
        self.logoutBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(49, 165, 25);\n"
"font-weight : 500;\n"
"font-size: 9pt;")
        self.logoutBtn.setObjectName("logoutBtn")
        self.accountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.accountBtn.setGeometry(QtCore.QRect(850, 290, 91, 50))
        self.accountBtn.setStyleSheet("border-color : rgb(4, 84, 83);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(4, 84, 83);\n"
"font-weight : 500;\n"
"font-size: 9pt;")
        self.accountBtn.setObjectName("accountBtn")
        self.cartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cartBtn.setGeometry(QtCore.QRect(850, 170, 91, 50))
        self.cartBtn.setStyleSheet("border-color: rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(49, 165, 25);\n"
"font-weight : 500;\n"
"font-size: 10pt;")
        self.cartBtn.setObjectName("cartBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(850, 560, 91, 50))
        self.backBtn.setStyleSheet("border-color: rgb(4, 84, 83);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color: rgb(4, 84, 83);\n"
"font-weight : 500;\n"
"font-size: 10pt;")
        self.backBtn.setObjectName("backBtn")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(20, 10, 321, 61))
        self.mainTitle.setStyleSheet("border-color: rgb(4, 84, 83);\n"
"background-color: rgb(255, 255, 255);\n"
"border-style : solid;\n"
"border-width : 2px;\n"
"border-right-width : 0px;\n"
"border-bottom-width : 0px;\n"
"border-top-left-radius : 20px;\n"
"border-bottom-right-radius: 20px;\n"
"text-align: center;\n"
"")
        self.mainTitle.setObjectName("mainTitle")
        self.windowTitle = QtWidgets.QLabel(self.centralwidget)
        self.windowTitle.setGeometry(QtCore.QRect(400, 30, 181, 41))
        self.windowTitle.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"text-align: center;\n"
"color : rgb(49, 165, 25);")
        self.windowTitle.setObjectName("windowTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 242, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 153, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 242, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 242, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 153, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 242, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 242, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 153, 159))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 115, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 230, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.menubar.setPalette(palette)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # /////////////////////////////connect buttons to methods//////////////////////////////
        self.orderBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "order"))
        self.cartBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "cart"))
        self.historyBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "history"))
        self.accountBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "userInfo"))
        self.logoutBtn.clicked.connect(partial(logout, MainWindow))
        self.backBtn.clicked.connect(partial(Routing.RedirectBack, MainWindow))

        self.browseBtn.clicked.connect(partial(browse, MainWindow, self))
        self.submitBtn.clicked.connect(partial(submit, MainWindow, self))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.firstNameLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">First Name</span></p></body></html>"))
        self.lastNameLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Last Name</span></p></body></html>"))
        self.phoneNumberLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Phone Number</span></p></body></html>"))
        self.socialNumberLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Social Number</span></p></body></html>"))
        self.emailLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Email</span></p></body></html>"))
        self.newPasswordLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">New Password</span></p></body></html>"))
        self.passwordLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Password</span></p></body></html>"))
        self.imageLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Image</span></p></body></html>"))
        self.browseBtn.setText(_translate("MainWindow", "Browse"))
        self.submitBtn.setText(_translate("MainWindow", "Submit"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">{Restaurant.Name()}</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">Account Info</span></p></body></html>"))

        #////////////////run init////////////////////
        init(MainWindow, self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
