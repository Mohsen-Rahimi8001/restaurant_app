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
from Controllers.Admin.GiftCardController import GiftCardController
from Controllers.User.OrderController import OrderController



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    #set total price
    user = Auth.GetUser()

    totalPrice = user.getCartTotalSalePrice()
    if Transfer.Exists("invoice_discount_coefficient"):
        discount = Transfer.Get("invoice_discount_coefficient")
        Transfer.Add("invoice_discount_coefficient", discount)
        totalPrice = round( totalPrice * discount)

    setTotalPrice(ui, totalPrice)

    #display foods
    foods = user.getCartFoodObjects()

    for food in foods:
        ui.addFoodWidget(window, food, user.countFood(food))



def confirm(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    paymentMethod = getPaymentMethod(ui)
    accountNumber = getAccountNumber(ui)

    result = OrderController.ConfirmPayment(paymentMethod, accountNumber)

    if result:

        user = Auth.GetUser()

        #clear cart
        user.clearCart()

        #add order to users orders
        user.addOrder(result)

        Messages.push(Messages.Type.SUCCESS, "order booked")

        if Transfer.Exists("invoice_discount_coefficient"):
            Transfer.Get("invoice_discount_coefficient")

        Routing.Redirect(window, "history")

    else:
        Routing.Refresh(window)



def cancel(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):
    if Transfer.Exists("invoice_discount_coefficient"):
        Transfer.Get("invoice_discount_coefficient")
    Routing.Redirect(window, "cart")



def evaluate(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    code = getGiftCard(ui)
    if not code:
        return

    result = GiftCardController.Evaluate(code)

    if result:
        Transfer.Add("invoice_discount_coefficient", (100 - int(result)) / 100 )
        Messages.push(Messages.Type.SUCCESS, "your gift cart evaluated successfully")

    Routing.Refresh(window)



def logout(window : QtWidgets.QMainWindow):

    questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
    if questionResult:
        if Transfer.Exists("invoice_discount_coefficient"):
            Transfer.Get("invoice_discount_coefficient")
        Auth.LogOut()
        Routing.ClearStack()
        Routing.Redirect(window, "login")




#input functions


def setTotalPrice(ui : "Ui_MainWindow", value : str):
    ui.totalPriceValue.setText(str( value ))


def getGiftCard(ui : "Ui_MainWindow"):
    return ui.giftCardEdit.text().strip()


def setGiftCard(ui : "Ui_MainWindow", value : str):
    ui.giftCardEdit.setText( str(value) )


def getAccountNumber(ui : "Ui_MainWindow"):
    return ui.accountNumberEdit.text().strip()


def setAccountNumber(ui : "Ui_MainWindow", value : str):
    ui.accountNumberEdit.setText( str(value) )


def getPaymentMethod(ui : "Ui_MainWindow"):

    if not ui.onlineRadio.isChecked() and not ui.onSpotRadio.isChecked():
        return -1

    if ui.onlineRadio.isChecked():
        return 0

    elif ui.onSpotRadio.isChecked():
        return 1


def setPaymentMethod(ui : "Ui_MainWindow", value : int):

    if value == 0:
        ui.onlineRadio.setChecked(True)
        ui.onSpotRadio.setChecked(False)

    elif value == 1:
        ui.onlineRadio.setChecked(False)
        ui.onSpotRadio.setChecked(True)



#////////////////////////////////////ui/////////////////////////////////////


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    def addFoodWidget(self, window : QtWidgets.QMainWindow, food : Food, count : int):


        self.foodWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.foodWidget.setMinimumSize(QtCore.QSize(0, 51))
        self.foodWidget.setMaximumSize(QtCore.QSize(16777215, 51))
        self.foodWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border-width : 0px;\n"
                                      "border-style : solid;\n"
                                      "\n"
                                      "")
        self.foodWidget.setObjectName("foodWidget")
        self.foodFee = QtWidgets.QLabel(self.foodWidget)
        self.foodFee.setGeometry(QtCore.QRect(400, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodFee.sizePolicy().hasHeightForWidth())
        self.foodFee.setSizePolicy(sizePolicy)
        self.foodFee.setMinimumSize(QtCore.QSize(0, 0))
        self.foodFee.setStyleSheet("border-width:0px;\n"
                                   "background-color: rgb(245, 247, 250);\n"
                                   "border-color: rgb(5, 85, 82);\n"
                                   "border-radius:0px;\n"
                                   "background-color: rgb(245, 247, 250);\n"
                                   "")
        self.foodFee.setObjectName("foodFee")
        self.divider1 = QtWidgets.QWidget(self.foodWidget)
        self.divider1.setGeometry(QtCore.QRect(360, 10, 20, 31))
        self.divider1.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider1.setObjectName("divider1")
        self.divider2 = QtWidgets.QWidget(self.foodWidget)
        self.divider2.setGeometry(QtCore.QRect(550, 10, 20, 31))
        self.divider2.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider2.setObjectName("divider2")
        self.divider3 = QtWidgets.QWidget(self.foodWidget)
        self.divider3.setGeometry(QtCore.QRect(170, 10, 20, 31))
        self.divider3.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider3.setObjectName("divider3")
        self.foodCount = QtWidgets.QLabel(self.foodWidget)
        self.foodCount.setGeometry(QtCore.QRect(210, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodCount.sizePolicy().hasHeightForWidth())
        self.foodCount.setSizePolicy(sizePolicy)
        self.foodCount.setMinimumSize(QtCore.QSize(0, 0))
        self.foodCount.setStyleSheet("border-width:0px;\n"
                                     "background-color: rgb(245, 247, 250);\n"
                                     "border-color: rgb(5, 85, 82);\n"
                                     "border-radius:0px;\n"
                                     "background-color: rgb(245, 247, 250);\n"
                                     "")
        self.foodCount.setObjectName("foodCount")
        self.foodItem = QtWidgets.QLabel(self.foodWidget)
        self.foodItem.setGeometry(QtCore.QRect(589, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodItem.sizePolicy().hasHeightForWidth())
        self.foodItem.setSizePolicy(sizePolicy)
        self.foodItem.setMinimumSize(QtCore.QSize(0, 0))
        self.foodItem.setStyleSheet("border-width:0px;\n"
                                    "background-color: rgb(245, 247, 250);\n"
                                    "border-color: rgb(5, 85, 82);\n"
                                    "border-radius:0px;\n"
                                    "background-color: rgb(245, 247, 250);\n"
                                    "")
        self.foodItem.setObjectName("foodItem")
        self.foodTotalPrice = QtWidgets.QLabel(self.foodWidget)
        self.foodTotalPrice.setGeometry(QtCore.QRect(10, 10, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodTotalPrice.sizePolicy().hasHeightForWidth())
        self.foodTotalPrice.setSizePolicy(sizePolicy)
        self.foodTotalPrice.setMinimumSize(QtCore.QSize(0, 0))
        self.foodTotalPrice.setStyleSheet("border-width:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "")
        self.foodTotalPrice.setObjectName("foodTotalPrice")
        self.verticalLayout.addWidget(self.foodWidget)



        #set widget texts
        self.foodFee.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{food.sale_price}</span></p></body></html>")
        self.foodCount.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{count}</span></p></body></html>")
        self.foodItem.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{food.title}</span></p></body></html>")
        self.foodTotalPrice.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{ int(food.sale_price) * int(count) }</span></p></body></html>")


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
        self.cancelBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cancelBtn.setGeometry(QtCore.QRect(670, 90, 121, 41))
        self.cancelBtn.setStyleSheet("border-width:0px;\n"
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
        self.cancelBtn.setObjectName("cancelBtn")
        self.totalPriceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalPriceLabel.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.totalPriceLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.totalPriceLabel.setObjectName("totalPriceLabel")
        self.totalPriceValue = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalPriceValue.setGeometry(QtCore.QRect(130, 20, 271, 41))
        self.totalPriceValue.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.totalPriceValue.setObjectName("totalPriceValue")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 330, 771, 191))
        self.scrollArea_2.setStyleSheet("border-radius : 0px;\n"
"border-width : 0px;\n"
"border-left-width : 1px;\n"
"border-right-width : 1px;\n"
"background-color: rgb(245, 247, 250);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 769, 189))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")




        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.giftCardEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.giftCardEdit.setGeometry(QtCore.QRect(130, 110, 271, 31))
        self.giftCardEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.giftCardEdit.setObjectName("giftCardEdit")
        self.evaluateBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.evaluateBtn.setGeometry(QtCore.QRect(400, 110, 101, 31))
        self.evaluateBtn.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.evaluateBtn.setObjectName("evaluateBtn")
        self.giftCardLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.giftCardLabel.setGeometry(QtCore.QRect(30, 110, 101, 31))
        self.giftCardLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.giftCardLabel.setObjectName("giftCardLabel")
        self.accountNumberEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.accountNumberEdit.setGeometry(QtCore.QRect(370, 200, 231, 31))
        self.accountNumberEdit.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"padding-left:20px;\n"
"")
        self.accountNumberEdit.setObjectName("accountNumberEdit")
        self.accountNumberLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.accountNumberLabel.setGeometry(QtCore.QRect(260, 200, 111, 31))
        self.accountNumberLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.accountNumberLabel.setObjectName("accountNumberLabel")
        self.onSpotRadio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.onSpotRadio.setGeometry(QtCore.QRect(150, 170, 95, 20))
        self.onSpotRadio.setStyleSheet("border-top-width : 0px;\n"
"border-bottom-width : 1px;")
        self.onSpotRadio.setObjectName("onSpotRadio")
        self.pymentMethodLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pymentMethodLabel.setGeometry(QtCore.QRect(30, 170, 101, 61))
        self.pymentMethodLabel.setStyleSheet("border-width:0px;\n"
"border-bottom-width : 1px;\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(202, 205, 210);\n"
"\n"
"")
        self.pymentMethodLabel.setObjectName("pymentMethodLabel")
        self.onlineRadio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.onlineRadio.setGeometry(QtCore.QRect(150, 209, 95, 21))
        self.onlineRadio.setStyleSheet("border-top-width : 0px;\n"
"border-bottom-width : 1px;")
        self.onlineRadio.setObjectName("onlineRadio")
        self.foodWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.foodWidget_2.setGeometry(QtCore.QRect(40, 290, 747, 51))
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
        self.foodTitleFee = QtWidgets.QLabel(self.foodWidget_2)
        self.foodTitleFee.setGeometry(QtCore.QRect(400, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodTitleFee.sizePolicy().hasHeightForWidth())
        self.foodTitleFee.setSizePolicy(sizePolicy)
        self.foodTitleFee.setMinimumSize(QtCore.QSize(0, 0))
        self.foodTitleFee.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.foodTitleFee.setObjectName("foodTitleFee")
        self.divider1_2 = QtWidgets.QWidget(self.foodWidget_2)
        self.divider1_2.setGeometry(QtCore.QRect(360, 10, 20, 31))
        self.divider1_2.setStyleSheet("border-width : 0px;\n"
"border-right-width : 2px;\n"
"border-color: rgb(202, 205, 210);")
        self.divider1_2.setObjectName("divider1_2")
        self.divider2_2 = QtWidgets.QWidget(self.foodWidget_2)
        self.divider2_2.setGeometry(QtCore.QRect(550, 10, 20, 31))
        self.divider2_2.setStyleSheet("border-width : 0px;\n"
"border-right-width : 2px;\n"
"border-color: rgb(202, 205, 210);")
        self.divider2_2.setObjectName("divider2_2")
        self.divider3_2 = QtWidgets.QWidget(self.foodWidget_2)
        self.divider3_2.setGeometry(QtCore.QRect(170, 10, 20, 31))
        self.divider3_2.setStyleSheet("border-width : 0px;\n"
"border-right-width : 2px;\n"
"border-color: rgb(202, 205, 210);")
        self.divider3_2.setObjectName("divider3_2")
        self.foodTitleCount = QtWidgets.QLabel(self.foodWidget_2)
        self.foodTitleCount.setGeometry(QtCore.QRect(210, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodTitleCount.sizePolicy().hasHeightForWidth())
        self.foodTitleCount.setSizePolicy(sizePolicy)
        self.foodTitleCount.setMinimumSize(QtCore.QSize(0, 0))
        self.foodTitleCount.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.foodTitleCount.setObjectName("foodTitleCount")
        self.foodTitleItem = QtWidgets.QLabel(self.foodWidget_2)
        self.foodTitleItem.setGeometry(QtCore.QRect(589, 10, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodTitleItem.sizePolicy().hasHeightForWidth())
        self.foodTitleItem.setSizePolicy(sizePolicy)
        self.foodTitleItem.setMinimumSize(QtCore.QSize(0, 0))
        self.foodTitleItem.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.foodTitleItem.setObjectName("foodTitleItem")
        self.foodTitleTotalPrice = QtWidgets.QLabel(self.foodWidget_2)
        self.foodTitleTotalPrice.setGeometry(QtCore.QRect(10, 10, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodTitleTotalPrice.sizePolicy().hasHeightForWidth())
        self.foodTitleTotalPrice.setSizePolicy(sizePolicy)
        self.foodTitleTotalPrice.setMinimumSize(QtCore.QSize(0, 0))
        self.foodTitleTotalPrice.setStyleSheet("border-width:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"border-color: rgb(5, 85, 82);\n"
"border-radius:0px;\n"
"background-color: rgb(245, 247, 250);\n"
"")
        self.foodTitleTotalPrice.setObjectName("foodTitleTotalPrice")
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


        self.confirmBtn.clicked.connect( partial( confirm, MainWindow, self ) )
        self.cancelBtn.clicked.connect( partial( cancel, MainWindow, self ) )
        self.evaluateBtn.clicked.connect( partial( evaluate, MainWindow, self ) )


        self.retranslateUi(MainWindow)

        # ////////////////run init////////////////////
        init(MainWindow, self)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.confirmBtn.setText(_translate("MainWindow", "Confirm"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.totalPriceLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Total Price</span></p></body></html>"))
        self.totalPriceValue.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\"></span></p></body></html>"))
        self.evaluateBtn.setText(_translate("MainWindow", "Evaluate"))
        self.giftCardLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Gift Card</span></p></body></html>"))
        self.accountNumberLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Account Number : </span></p></body></html>"))
        self.onSpotRadio.setText(_translate("MainWindow", "on the spot"))
        self.pymentMethodLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055453;\">payment</span></p><p align=\"center\"><span style=\" color:#055453;\">method</span></p></body></html>"))
        self.onlineRadio.setText(_translate("MainWindow", "online"))
        self.foodTitleFee.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">fee</span></p></body></html>"))
        self.foodTitleCount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">count</span></p></body></html>"))
        self.foodTitleItem.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Item</span></p></body></html>"))
        self.foodTitleTotalPrice.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">total price</span></p></body></html>"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">Restaurant Title</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">Invoice</span></p></body></html>"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



