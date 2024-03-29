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
from Controllers.User.CartController import Cart



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    if not Transfer.Exists("menu_id"):
        return

    #get menu from Transfer
    menuId = Transfer.Get("menu_id")
    Transfer.Add("menu_id", menuId)

    menu = Menu.Get(menuId)


    #set labels
    setMenuTitle(ui, menu.title)
    setMenuDate(ui, menu.date)

    #get foods
    foods = menu.getFoods()

    for food in foods:
        ui.addFoodWidget(window, food)






def addToCart(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):

    #get menu date
    menuId = Transfer.Get("menu_id")
    Transfer.Add("menu_id", menuId)
    date = Menu.Get(menuId).date

    result = Cart.ReserveFood(food, date)

    if result:
        Messages.push(Messages.Type.SUCCESS, f"{food.title} added to your cart")

    Routing.Refresh(window)




def moreInfo(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", food : Food):

    Transfer.Add("food_info_id", food.id)
    Routing.Redirect(window, "foodInfo")




def logout(window : QtWidgets.QMainWindow):

    questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
    if questionResult:
        Auth.LogOut()
        Routing.ClearStack()
        Routing.Redirect(window, "login")




#input functions


def setMenuTitle(ui : "Ui_MainWindow", value : str):
    ui.menuTitleValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{value}</span></p></body></html>")

def setMenuDate(ui : "Ui_MainWindow", value : str):
    ui.menuDateValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{value}</span></p></body></html>")





#////////////////////////////////////ui/////////////////////////////////////


class Ui_MainWindow(object):




    def addFoodWidget(self, window : QtWidgets.QMainWindow, food : Food):

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
        self.foodStockValue = QtWidgets.QLabel(self.foodWidget)
        self.foodStockValue.setGeometry(QtCore.QRect(300, 60, 170, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodStockValue.sizePolicy().hasHeightForWidth())
        self.foodStockValue.setSizePolicy(sizePolicy)
        self.foodStockValue.setMinimumSize(QtCore.QSize(170, 0))
        self.foodStockValue.setStyleSheet("border-width:0px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "")
        self.foodStockValue.setObjectName("foodStockValue")
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
        self.foodStockLabel = QtWidgets.QLabel(self.foodWidget)
        self.foodStockLabel.setGeometry(QtCore.QRect(200, 60, 101, 31))
        self.foodStockLabel.setStyleSheet("border-width:0px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(202, 205, 210);\n"
                                          "\n"
                                          "")
        self.foodStockLabel.setObjectName("foodStockLabel")
        self.foodImage = QtWidgets.QLabel(self.foodWidget)
        self.foodImage.setGeometry(QtCore.QRect(510, 20, 181, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodImage.sizePolicy().hasHeightForWidth())
        self.foodImage.setSizePolicy(sizePolicy)
        self.foodImage.setMinimumSize(QtCore.QSize(0, 111))
        self.foodImage.setStyleSheet("background-color: rgb(245, 247, 250);\n"
                                     "border-width : 0px;")
        self.foodImage.setText("")
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
        self.foodAddBtn.setGeometry(QtCore.QRect(32, 20, 101, 51))
        self.foodAddBtn.setStyleSheet("border-width:0px;\n"
                                      "border-bottom-width : 5px;\n"
                                      "border-color: rgb(5, 85, 82);\n"
                                      "border-radius:0px;\n"
                                      "background-color: rgb(245, 247, 250);\n"
                                      "padding-left:0px;\n"
                                      "")
        self.foodAddBtn.setObjectName("foodAddBtn")
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



        #add label values
        self.foodTitleLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Title : </span></p></body></html>")
        self.foodStockValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span>{food.stock}</p></body></html>")
        self.foodTitleValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span>{food.title}</p></body></html>")
        self.foodPriceLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Price : </span></p></body></html>")
        self.foodPriceValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{food.sale_price}</span></p></body></html>")
        self.foodStockLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Stock : </span></p></body></html>")
        self.foodAddBtn.setText("Add To Cart")
        self.foodInfoBtn.setText("More Info")

        self.foodImage.setPixmap(QtGui.QPixmap( food.image ))
        self.foodImage.setScaledContents(True)



        #connect buttons
        self.foodAddBtn.clicked.connect( partial( addToCart, window, self, food ) )
        self.foodInfoBtn.clicked.connect( partial( moreInfo, window, self, food ) )

        #add widget to list
        self.foodsList.append(self.foodWidget)













    def setupUi(self, MainWindow):


        self.foodsList = []

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
        self.menuTitleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.menuTitleLabel.setGeometry(QtCore.QRect(30, 30, 101, 31))
        self.menuTitleLabel.setStyleSheet("border-width:0px;\n"
                                          "border-bottom-width : 1px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(202, 205, 210);\n"
                                          "\n"
                                          "")
        self.menuTitleLabel.setObjectName("menuTitleLabel")
        self.menuTitleValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.menuTitleValue.setGeometry(QtCore.QRect(130, 30, 221, 31))
        self.menuTitleValue.setStyleSheet("border-width:0px;\n"
                                          "border-bottom-width : 1px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "padding-left:20px;\n"
                                          "")
        self.menuTitleValue.setObjectName("menuTitleValue")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 80, 771, 441))
        self.scrollArea_2.setStyleSheet("border-radius : 0px;\n"
                                        "border-width : 0px;\n"
                                        "border-top-width : 1px;\n"
                                        "background-color: rgb(245, 247, 250);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 769, 439))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")






        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.menuDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.menuDateLabel.setGeometry(QtCore.QRect(380, 30, 101, 31))
        self.menuDateLabel.setStyleSheet("border-width:0px;\n"
                                         "border-bottom-width : 1px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(202, 205, 210);\n"
                                         "\n"
                                         "")
        self.menuDateLabel.setObjectName("menuDateLabel")
        self.menuDateValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.menuDateValue.setGeometry(QtCore.QRect(480, 30, 221, 31))
        self.menuDateValue.setStyleSheet("border-width:0px;\n"
                                         "border-bottom-width : 1px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(245, 247, 250);\n"
                                         "padding-left:20px;\n"
                                         "")
        self.menuDateValue.setObjectName("menuDateValue")
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
        self.orderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.orderBtn.setGeometry(QtCore.QRect(850, 110, 91, 50))
        self.orderBtn.setStyleSheet("border-color: rgb(49, 165, 25);\n"
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
        self.cartBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cartBtn.setGeometry(QtCore.QRect(850, 170, 91, 50))
        self.cartBtn.setStyleSheet("border-color : rgb(49, 165, 25);\n"
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

        self.retranslateUi(MainWindow)

        # ////////////////run init////////////////////
        init(MainWindow, self)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTitleLabel.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Menu Title</span></p></body></html>"))
        self.menuTitleValue.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.menuDateLabel.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Menu Date</span></p></body></html>"))
        self.menuDateValue.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">{Restaurant.Name()}</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">MENU</span></p></body></html>"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
