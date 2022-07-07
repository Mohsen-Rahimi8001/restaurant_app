from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Window import Routing
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Lib.Questions import Questions
from Lib.Image import Image
from Models.Restaurant import Restaurant
from Models.Food import Food
from Window import Transfer



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):
    pass



def logout(window : QtWidgets.QMainWindow):

    questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
    if questionResult:
        Auth.LogOut()
        Routing.ClearStack()
        Routing.Redirect(window, "login")




#////////////////////////////////////ui/////////////////////////////////////
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
"color : rgb(49, 165, 25);\n"
"font-weight : 500;\n"
"font-size: 10pt;")
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
        self.imageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageLabel.setGeometry(QtCore.QRect(50, 40, 181, 131))
        self.imageLabel.setStyleSheet("border-width : 0px;\n"
"border-radius:0px;")
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.titleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.titleLabel.setGeometry(QtCore.QRect(40, 200, 101, 31))
        self.titleLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.titleLabel.setObjectName("titleLabel")
        self.titleValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.titleValue.setGeometry(QtCore.QRect(140, 200, 221, 31))
        self.titleValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.titleValue.setObjectName("titleValue")
        self.priceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.priceLabel.setGeometry(QtCore.QRect(390, 200, 101, 31))
        self.priceLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.priceLabel.setObjectName("priceLabel")
        self.priceValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.priceValue.setGeometry(QtCore.QRect(490, 200, 221, 31))
        self.priceValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.priceValue.setObjectName("priceValue")
        self.categoryLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.categoryLabel.setGeometry(QtCore.QRect(40, 250, 101, 31))
        self.categoryLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.categoryLabel.setObjectName("categoryLabel")
        self.categoryValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.categoryValue.setGeometry(QtCore.QRect(140, 250, 221, 31))
        self.categoryValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.categoryValue.setObjectName("categoryValue")
        self.stockLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.stockLabel.setGeometry(QtCore.QRect(390, 250, 101, 31))
        self.stockLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.stockLabel.setObjectName("stockLabel")
        self.stockValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.stockValue.setGeometry(QtCore.QRect(490, 250, 221, 31))
        self.stockValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.stockValue.setObjectName("stockValue")
        self.descriptionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.descriptionLabel.setGeometry(QtCore.QRect(40, 300, 101, 31))
        self.descriptionLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.descriptionValue.setGeometry(QtCore.QRect(140, 300, 221, 211))
        self.descriptionValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.descriptionValue.setObjectName("descriptionValue")
        self.materialsValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.materialsValue.setGeometry(QtCore.QRect(490, 300, 221, 211))
        self.materialsValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.materialsValue.setObjectName("materialsValue")
        self.materialsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.materialsLabel.setGeometry(QtCore.QRect(390, 300, 101, 31))
        self.materialsLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.materialsLabel.setObjectName("materialsLabel")
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
        self.accountBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(49, 165, 25);\n"
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Title : </span></p></body></html>"))
        self.titleValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.priceLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Price : </span></p></body></html>"))
        self.priceValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.categoryLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Category :</span></p></body></html>"))
        self.categoryValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.stockLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">stock :</span></p></body></html>"))
        self.stockValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.descriptionLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Description :</span></p></body></html>"))
        self.descriptionValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.materialsValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.materialsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Materials :</span></p></body></html>"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">Restaurant Title</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">Food title</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

