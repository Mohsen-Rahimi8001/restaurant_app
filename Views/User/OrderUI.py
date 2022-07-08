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
from Models.Menu import Menu
from Controllers.User.MenuController import MenuController



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    if Transfer.Exists("date_search_data"):
        data = Transfer.Get("date_search_data")
        setDay(ui, data["day"])
        setMonth(ui, data["month"])
        setYear(ui, data["year"])


    menus = MenuController.GetPresentMenus()

    if Transfer.Exists("order_type"):

        orderType = Transfer.Get("order_type")

        if orderType == "search_date" or orderType == "search_food":

            menus = Transfer.Get("order_menus")


    for menu in menus:
        ui.addMenu(window, menu)




def searchDate(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    year = getYear(ui)
    month = getMonth(ui)
    day = getDay(ui)

    menus = MenuController.SearchDate(year, month, day)

    if menus:

        Transfer.Add("order_type", "search_date")
        Transfer.Add("order_menus", menus)

    Transfer.Add("date_search_data", {"year": year, "month": month, "day": day})
    Routing.Refresh(window)





def searchFood(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    Routing.Redirect(window, "search")



def order(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", menu : Menu):

    Transfer.Add("menu_id", menu.id)
    Routing.Redirect(window, "menu")



def logout(window : QtWidgets.QMainWindow):

    questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
    if questionResult:
        Auth.LogOut()
        Routing.ClearStack()
        Routing.Redirect(window, "login")



#input methods

def getYear(ui : 'Ui_MainWindow'):
    return ui.yearEdit.text().strip()

def getMonth(ui : 'Ui_MainWindow'):
    return ui.monthEdit.text().strip()

def getDay(ui : 'Ui_MainWindow'):
    return ui.dayEdit.text().strip()


def setYear(ui : 'Ui_MainWindow', value : str):
    return ui.yearEdit.setText(str(value))

def setMonth(ui : 'Ui_MainWindow', value : str):
    return ui.monthEdit.setText(str(value))

def setDay(ui : 'Ui_MainWindow', value : str):
    return ui.dayEdit.setText(str(value))




#////////////////////////////////////ui/////////////////////////////////////



class Ui_MainWindow(object):

    def addMenu(self, window : QtWidgets.QMainWindow, menu : Menu):


        self.menuWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.menuWidget.setMinimumSize(QtCore.QSize(0, 51))
        self.menuWidget.setMaximumSize(QtCore.QSize(16777215, 51))
        self.menuWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-width : 0px;\n"
                                      "border-style : solid;\n"
                                      "\n"
                                      "")
        self.menuWidget.setObjectName("menuWidget")
        self.menuDateLabel = QtWidgets.QLabel(self.menuWidget)
        self.menuDateLabel.setGeometry(QtCore.QRect(290, 10, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuDateLabel.sizePolicy().hasHeightForWidth())
        self.menuDateLabel.setSizePolicy(sizePolicy)
        self.menuDateLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.menuDateLabel.setStyleSheet("border-width:0px;\n"
                                         "background-color: rgb(245, 247, 250);\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(245, 247, 250);\n"
                                         "")
        self.menuDateLabel.setObjectName("menuDateLabel")
        self.divider1 = QtWidgets.QWidget(self.menuWidget)
        self.divider1.setGeometry(QtCore.QRect(250, 10, 20, 31))
        self.divider1.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider1.setObjectName("divider1")
        self.divider2 = QtWidgets.QWidget(self.menuWidget)
        self.divider2.setGeometry(QtCore.QRect(500, 10, 20, 31))
        self.divider2.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider2.setObjectName("divider2")
        self.menuTitleLabel = QtWidgets.QLabel(self.menuWidget)
        self.menuTitleLabel.setGeometry(QtCore.QRect(539, 10, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuTitleLabel.sizePolicy().hasHeightForWidth())
        self.menuTitleLabel.setSizePolicy(sizePolicy)
        self.menuTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.menuTitleLabel.setStyleSheet("border-width:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "")
        self.menuTitleLabel.setObjectName("menuTitleLabel")
        self.menuBtn = QtWidgets.QPushButton(self.menuWidget)
        self.menuBtn.setGeometry(QtCore.QRect(30, 10, 211, 31))
        self.menuBtn.setStyleSheet("border-width:0px;\n"
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
        self.menuBtn.setObjectName("menuBtn")
        self.verticalLayout.addWidget(self.menuWidget)


        #//////////add data to menu widget//////////////
        self.menuDateLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{menu.date}</span></p></body></html>")
        self.menuTitleLabel.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{menu.title}</span></p></body></html>")
        self.menuBtn.setText("Order form This Menu")


        #connect buttons to methods
        self.menuBtn.clicked.connect(partial( order, window, self, menu ))


        #add menu to list
        self.menuWidgets.append(self.menuWidget)














    def setupUi(self, MainWindow):


        #list of menu widgets
        self.menuWidgets = []




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
        self.orderBtn.setStyleSheet("border-color: rgb(4, 84, 83);\n"
"background-color: rgb(245, 247, 250);\n"
"border-style : solid;\n"
"border-bottom-width : 2px;\n"
"border-right-width : 2px;\n"
"border-bottom-right-radius: 20px;\n"
"box-shadow: 10px 10px 5px -5px #666;\n"
"color : rgb(4, 84, 83);\n"
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
        self.dayEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.dayEdit.setGeometry(QtCore.QRect(210, 20, 51, 31))
        self.dayEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.dayEdit.setObjectName("dayEdit")
        self.searchDateBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.searchDateBtn.setGeometry(QtCore.QRect(30, 20, 121, 31))
        self.searchDateBtn.setStyleSheet("border-width:0px;\n"
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
        self.searchDateBtn.setObjectName("searchDateBtn")
        self.dayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dayLabel.setGeometry(QtCore.QRect(160, 20, 51, 31))
        self.dayLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.dayLabel.setObjectName("dayLabel")
        self.monthEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.monthEdit.setGeometry(QtCore.QRect(320, 20, 51, 31))
        self.monthEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.monthEdit.setObjectName("monthEdit")
        self.monthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.monthLabel.setGeometry(QtCore.QRect(270, 20, 51, 31))
        self.monthLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.monthLabel.setObjectName("monthLabel")
        self.yearEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.yearEdit.setGeometry(QtCore.QRect(430, 20, 51, 31))
        self.yearEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.yearEdit.setObjectName("yearEdit")
        self.yearLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.yearLabel.setGeometry(QtCore.QRect(380, 20, 51, 31))
        self.yearLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.yearLabel.setObjectName("yearLabel")
        self.SearchFoodBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.SearchFoodBtn.setGeometry(QtCore.QRect(610, 20, 201, 31))
        self.SearchFoodBtn.setStyleSheet("border-width:0px;\n"
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
        self.SearchFoodBtn.setObjectName("SearchFoodBtn")
        self.foodWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.foodWidget_2.setGeometry(QtCore.QRect(40, 110, 747, 51))
        self.foodWidget_2.setMinimumSize(QtCore.QSize(0, 51))
        self.foodWidget_2.setMaximumSize(QtCore.QSize(16777215, 51))
        self.foodWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-width : 2px;\n"
"border-radius : 0;\n"
"border-style : solid;\n"
"border-color: rgb(5, 85, 82);\n"
"\n"
"")
        self.foodWidget_2.setObjectName("foodWidget_2")
        self.menuDateTitleLabel = QtWidgets.QLabel(self.foodWidget_2)
        self.menuDateTitleLabel.setGeometry(QtCore.QRect(290, 10, 201, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuDateTitleLabel.sizePolicy().hasHeightForWidth())
        self.menuDateTitleLabel.setSizePolicy(sizePolicy)
        self.menuDateTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.menuDateTitleLabel.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.menuDateTitleLabel.setObjectName("menuDateTitleLabel")
        self.divider1_2 = QtWidgets.QWidget(self.foodWidget_2)
        self.divider1_2.setGeometry(QtCore.QRect(250, 10, 20, 31))
        self.divider1_2.setStyleSheet("border-width : 0px;\n"
"border-right-width : 2px;\n"
"border-color: rgb(202, 205, 210);")
        self.divider1_2.setObjectName("divider1_2")
        self.divider2_2 = QtWidgets.QWidget(self.foodWidget_2)
        self.divider2_2.setGeometry(QtCore.QRect(500, 10, 20, 31))
        self.divider2_2.setStyleSheet("border-width : 0px;\n"
"border-right-width : 2px;\n"
"border-color: rgb(202, 205, 210);")
        self.divider2_2.setObjectName("divider2_2")
        self.orderTitleLabel = QtWidgets.QLabel(self.foodWidget_2)
        self.orderTitleLabel.setGeometry(QtCore.QRect(30, 10, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderTitleLabel.sizePolicy().hasHeightForWidth())
        self.orderTitleLabel.setSizePolicy(sizePolicy)
        self.orderTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.orderTitleLabel.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.orderTitleLabel.setObjectName("orderTitleLabel")
        self.menuTitleTitleLabel = QtWidgets.QLabel(self.foodWidget_2)
        self.menuTitleTitleLabel.setGeometry(QtCore.QRect(539, 10, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuTitleTitleLabel.sizePolicy().hasHeightForWidth())
        self.menuTitleTitleLabel.setSizePolicy(sizePolicy)
        self.menuTitleTitleLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.menuTitleTitleLabel.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.menuTitleTitleLabel.setObjectName("menuTitleTitleLabel")
        self.menusScrollArea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.menusScrollArea.setGeometry(QtCore.QRect(30, 170, 771, 381))
        self.menusScrollArea.setStyleSheet("border-radius : 0px;\n"
"border-width : 0px;\n"
"border-left-width : 1px;\n"
"border-right-width : 1px;\n"
"background-color: rgb(245, 247, 250);")
        self.menusScrollArea.setWidgetResizable(True)
        self.menusScrollArea.setObjectName("menusScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 769, 379))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.menusScrollArea.setWidget(self.scrollAreaWidgetContents_3)
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




        # /////////////////////////////connect buttons to methods//////////////////////////////
        self.orderBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "order"))
        self.cartBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "cart"))
        self.historyBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "history"))
        self.accountBtn.clicked.connect(partial(Routing.Redirect, MainWindow, "userInfo"))
        self.logoutBtn.clicked.connect(partial(logout, MainWindow))
        self.backBtn.clicked.connect(partial(Routing.RedirectBack, MainWindow))

        self.searchDateBtn.clicked.connect(partial(searchDate, MainWindow, self))
        self.SearchFoodBtn.clicked.connect(partial(searchFood, MainWindow, self))

        self.retranslateUi(MainWindow)

        # ////////////////run init////////////////////
        init(MainWindow, self)





        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.searchDateBtn.setText(_translate("MainWindow", "Search Date"))
        self.dayLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">day</span></p></body></html>"))
        self.monthLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">month</span></p></body></html>"))
        self.yearEdit.setText(_translate("MainWindow", "2022"))
        self.yearLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">year</span></p></body></html>"))
        self.SearchFoodBtn.setText(_translate("MainWindow", "Search Food"))
        self.menuDateTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">menu date</span></p></body></html>"))
        self.orderTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">order</span></p></body></html>"))
        self.menuTitleTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">menu title</span></p></body></html>"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">{Restaurant.Name()}</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">Order</span></p></body></html>"))












if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())