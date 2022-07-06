from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Window import Routing
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Lib.Questions import Questions
from Lib.Image import Image
from Models.Restaurant import Restaurant
from Models.Food import Food



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


def confirm(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):
    pass


def clear(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):
        pass


def add(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):
        pass


def remove(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):
        pass


def reduce(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):
        pass


def info(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):
        pass





# get input methods





#////////////////////////////////////ui/////////////////////////////////////

class Ui_MainWindow(object):

    Foods = []

    def addFood(self, food : Food, count : int):
            """adds a food item to cart"""

            self.foodWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
            self.foodWidget.setMinimumSize(QtCore.QSize(0, 155))
            self.foodWidget.setMaximumSize(QtCore.QSize(16777215, 155))
            self.foodWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "border-width : 0px;\n"
    "border-style : solid;\n"
    "border-bottom-width : 2px;\n"
    "border-color: rgb(51, 165, 24);\n"
    "")
            self.foodWidget.setObjectName("foodWidget")
            self.foodTitleLabel = QtWidgets.QLabel(self.foodWidget)
            self.foodTitleLabel.setGeometry(QtCore.QRect(200, 20, 101, 31))
            self.foodTitleLabel.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(202, 205, 210);\n"
    "\n"
    "")
            self.foodTitleLabel.setObjectName("foodTitleLabel")
            self.foodNumberValue = QtWidgets.QLabel(self.foodWidget)
            self.foodNumberValue.setGeometry(QtCore.QRect(300, 60, 170, 31))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.foodNumberValue.sizePolicy().hasHeightForWidth())
            self.foodNumberValue.setSizePolicy(sizePolicy)
            self.foodNumberValue.setMinimumSize(QtCore.QSize(170, 0))
            self.foodNumberValue.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "")
            self.foodNumberValue.setObjectName("foodNumberValue")
            self.foodTitleValue = QtWidgets.QLabel(self.foodWidget)
            self.foodTitleValue.setGeometry(QtCore.QRect(300, 20, 170, 31))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.foodTitleValue.sizePolicy().hasHeightForWidth())
            self.foodTitleValue.setSizePolicy(sizePolicy)
            self.foodTitleValue.setMinimumSize(QtCore.QSize(170, 0))
            self.foodTitleValue.setStyleSheet("border-width:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "")
            self.foodTitleValue.setObjectName("foodTitleValue")
            self.foodPriceLabel = QtWidgets.QLabel(self.foodWidget)
            self.foodPriceLabel.setGeometry(QtCore.QRect(200, 100, 101, 31))
            self.foodPriceLabel.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(202, 205, 210);\n"
    "\n"
    "")
            self.foodPriceLabel.setObjectName("foodPriceLabel")
            self.foodPriceValue = QtWidgets.QLabel(self.foodWidget)
            self.foodPriceValue.setGeometry(QtCore.QRect(300, 100, 170, 31))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.foodPriceValue.sizePolicy().hasHeightForWidth())
            self.foodPriceValue.setSizePolicy(sizePolicy)
            self.foodPriceValue.setMinimumSize(QtCore.QSize(170, 0))
            self.foodPriceValue.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "")
            self.foodPriceValue.setObjectName("foodPriceValue")
            self.foodNumberLabel = QtWidgets.QLabel(self.foodWidget)
            self.foodNumberLabel.setGeometry(QtCore.QRect(200, 60, 101, 31))
            self.foodNumberLabel.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(202, 205, 210);\n"
    "\n"
    "")
            self.foodNumberLabel.setObjectName("foodNumberLabel")
            self.foodImage = QtWidgets.QLabel(self.foodWidget)
            self.foodImage.setGeometry(QtCore.QRect(510, 20, 181, 111))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.foodImage.sizePolicy().hasHeightForWidth())
            self.foodImage.setSizePolicy(sizePolicy)
            self.foodImage.setMinimumSize(QtCore.QSize(0, 111))
            self.foodImage.setObjectName("foodImage")
            self.divider1 = QtWidgets.QWidget(self.foodWidget)
            self.divider1.setGeometry(QtCore.QRect(150, 20, 20, 111))
            self.divider1.setStyleSheet("border-width : 0px;\n"
    "border-right-width : 2px;\n"
    "border-color: rgb(202, 205, 210);")
            self.divider1.setObjectName("divider1")
            self.divider2 = QtWidgets.QWidget(self.foodWidget)
            self.divider2.setGeometry(QtCore.QRect(470, 20, 20, 111))
            self.divider2.setStyleSheet("border-width : 0px;\n"
    "border-right-width : 2px;\n"
    "border-color: rgb(202, 205, 210);")
            self.divider2.setObjectName("divider2")
            self.foodAddBtn = QtWidgets.QPushButton(self.foodWidget)
            self.foodAddBtn.setGeometry(QtCore.QRect(32, 20, 101, 21))
            self.foodAddBtn.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "padding-left:0px;\n"
    "")
            self.foodAddBtn.setObjectName("foodAddBtn")
            self.foodRemoveBtn = QtWidgets.QPushButton(self.foodWidget)
            self.foodRemoveBtn.setGeometry(QtCore.QRect(30, 80, 101, 21))
            self.foodRemoveBtn.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "padding-left:0px;\n"
    "")
            self.foodRemoveBtn.setObjectName("foodRemoveBtn")
            self.foodReduceBtn = QtWidgets.QPushButton(self.foodWidget)
            self.foodReduceBtn.setGeometry(QtCore.QRect(30, 50, 101, 21))
            self.foodReduceBtn.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "padding-left:0px;\n"
    "")
            self.foodReduceBtn.setObjectName("foodReduceBtn")
            self.foodInfoBtn = QtWidgets.QPushButton(self.foodWidget)
            self.foodInfoBtn.setGeometry(QtCore.QRect(32, 110, 101, 21))
            self.foodInfoBtn.setStyleSheet("border-width:0px;\n"
    "border-color: rgb(5, 85, 82);\n"
    "border-radius:0px;\n"
    "background-color: rgb(245, 247, 250);\n"
    "padding-left:0px;\n"
    "")
            self.foodInfoBtn.setObjectName("foodInfoBtn")
            self.verticalLayout.addWidget(self.foodWidget)

            self.foodTitleLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Title : </span></p></body></html>")
            self.foodPriceLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Price : </span></p></body></html>")
            self.foodNumberLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Count : </span></p></body></html>")
            self.foodAddBtn.setText("Add")
            self.foodRemoveBtn.setText("Remove")
            self.foodReduceBtn.setText("Reduce")
            self.foodInfoBtn.setText("More Info")

            #set values

            self.foodNumberValue.setText(
                    f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{count}</span></p></body></html>")
            self.foodTitleValue.setText(
                    f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{food.title}</span></p></body></html>")
            self.foodPriceValue.setText(
                    f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{food.sale_price}</span></p></body></html>")

            self.foodImage.setPixmap(QtGui.QPixmap(food.image))
            self.foodImage.setScaledContents(True)


            #connect buttons

            self.foodAddBtn.clicked.connect(lambda:add(MainWindow, self, food))
            self.foodReduceBtn.clicked.connect(lambda:reduce(MainWindow, self, food))
            self.foodRemoveBtn.clicked.connect(lambda:remove(MainWindow, self, food))
            self.foodInfoBtn.clicked.connect(lambda:info(MainWindow, self, food))











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
        self.confirmBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.confirmBtn.setGeometry(QtCore.QRect(670, 30, 121, 41))
        self.confirmBtn.setStyleSheet("border-width:0px;\n"
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
        self.confirmBtn.setObjectName("confirmBtn")
        self.clearBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.clearBtn.setGeometry(QtCore.QRect(540, 30, 121, 41))
        self.clearBtn.setStyleSheet("border-width:0px;\n"
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
        self.clearBtn.setObjectName("clearBtn")
        self.totalPriceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalPriceLabel.setGeometry(QtCore.QRect(30, 30, 101, 41))
        self.totalPriceLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.totalPriceLabel.setObjectName("totalPriceLabel")
        self.totalPriceValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalPriceValue.setGeometry(QtCore.QRect(130, 30, 271, 41))
        self.totalPriceValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.totalPriceValue.setObjectName("totalPriceValue")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 90, 771, 431))
        self.scrollArea_2.setStyleSheet("border-radius : 0px;\n"
"border-width : 0px;\n"
"border-top-width : 1px;\n"
"background-color: rgb(245, 247, 250);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 769, 429))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")





















        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)


        self.historyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.historyBtn.setGeometry(QtCore.QRect(850, 230, 91, 50))
        self.historyBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
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
"color : rgb(49, 165, 25);\n"
"font-weight : 500;\n"
"font-size: 9pt;")
        self.accountBtn.setObjectName("accountBtn")
        self.cartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cartBtn.setGeometry(QtCore.QRect(850, 110, 91, 50))
        self.cartBtn.setStyleSheet("border-color: rgb(49, 165, 25);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
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
"text-align: center;\n"
"color : rgb(49, 165, 25);")
        self.windowTitle.setObjectName("windowTitle")
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(850, 170, 91, 50))
        self.orderBtn.setStyleSheet("border-color: rgb(4, 84, 83);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"color : rgb(4, 84, 83);\n"
"font-weight : 500;\n"
"font-size: 10pt;")
        self.orderBtn.setObjectName("orderBtn")
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

        self.confirmBtn.clicked.connect(partial(confirm, MainWindow, self))
        self.clearBtn.clicked.connect(partial(clear, MainWindow, self))




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.confirmBtn.setText(_translate("MainWindow", "Confirm"))
        self.clearBtn.setText(_translate("MainWindow", "Clear Cart"))
        self.totalPriceLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Total Price</span></p></body></html>"))
        self.totalPriceValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.cartBtn.setText(_translate("MainWindow", "ORDER"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">{Restaurant.Name()}</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">CART</span></p></body></html>"))
        self.orderBtn.setText(_translate("MainWindow", "CART"))

        # ////////////////run init////////////////////
        init(MainWindow, self)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
