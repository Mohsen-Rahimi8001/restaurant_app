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
from Models.Order import Order
from Lib.DateTools import DateTools



#///////////////////////////////EVENTS///////////////////////

# button events

def init(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow"):

    user = Auth.GetUser()

    orders = user.getOrders()

    for order in orders:

        #check for delivered orders
        if DateTools.Compare(DateTools.GetToday(), order.deliver_date) == -1:
            order.deliver()

        #show order
        if order.confirmed:

            if order.delivered:
                ui.addLabelOrderWidget(window, order, "Delivered")

            else:
                ui.addCancelOrderWidget(window, order)

        else:

            if order.delivered:
                ui.addLabelOrderWidget(window, order, "Rejected")

            else:
                ui.addLabelOrderWidget(window, order, "Processing")



def logout(window : QtWidgets.QMainWindow):

        questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure, you want to log out ?")
        if questionResult:
                Auth.LogOut()
                Routing.ClearStack()
                Routing.Redirect(window, "login")



def cancel(window : QtWidgets.QMainWindow, ui : "Ui_MainWindow", order : Order):

    questionResult = Questions.ask(Questions.Type.ASKYESNO, "are you sure you want ot delete this order")
    if questionResult:

        foods = order.getFoods()

        #add foods stock
        for food in foods:
            food.addToStock(1)

        user = Auth.GetUser()

        user.removeOrder(order)

        Order.Delete(order.id)

        Messages.push(Messages.Type.INFO, "order canceled")

        Routing.Refresh(window)








#////////////////////////////////////ui/////////////////////////////////////



class Ui_MainWindow(object):


    def addCancelOrderWidget(self, window : QtWidgets.QMainWindow, order : Order):

        self.cancelOrderWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.cancelOrderWidget.setMinimumSize(QtCore.QSize(0, 120))
        self.cancelOrderWidget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.cancelOrderWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-style : solid;\n"
                                             "border-bottom-width : 2px;\n"
                                             "border-color: rgb(51, 165, 24);")
        self.cancelOrderWidget.setObjectName("cancelOrderWidget")
        self.paymentLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.paymentLabel.setGeometry(QtCore.QRect(160, 20, 81, 21))
        self.paymentLabel.setStyleSheet("border-width:0px;\n"
                                        "border-color: rgb(5, 85, 82);\n"
                                        "border-radius:0px;\n"
                                        "background-color: rgb(202, 205, 210);\n"
                                        "\n"
                                        "")
        self.paymentLabel.setObjectName("paymentLabel")
        self.refNumValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.refNumValue.setGeometry(QtCore.QRect(240, 50, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refNumValue.sizePolicy().hasHeightForWidth())
        self.refNumValue.setSizePolicy(sizePolicy)
        self.refNumValue.setMinimumSize(QtCore.QSize(170, 0))
        self.refNumValue.setStyleSheet("border-width:0px;\n"
                                       "border-color: rgb(5, 85, 82);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(245, 247, 250);\n"
                                       "padding-left:20px;\n"
                                       "")
        self.refNumValue.setObjectName("refNumValue")
        self.paymentValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.paymentValue.setGeometry(QtCore.QRect(240, 20, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymentValue.sizePolicy().hasHeightForWidth())
        self.paymentValue.setSizePolicy(sizePolicy)
        self.paymentValue.setMinimumSize(QtCore.QSize(170, 0))
        self.paymentValue.setStyleSheet("border-width:0px;\n"
                                        "background-color: rgb(245, 247, 250);\n"
                                        "border-color: rgb(5, 85, 82);\n"
                                        "border-radius:0px;\n"
                                        "background-color: rgb(245, 247, 250);\n"
                                        "padding-left:20px;\n"
                                        "")
        self.paymentValue.setObjectName("paymentValue")
        self.accNumLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.accNumLabel.setGeometry(QtCore.QRect(160, 80, 81, 21))
        self.accNumLabel.setStyleSheet("border-width:0px;\n"
                                       "border-color: rgb(5, 85, 82);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(202, 205, 210);\n"
                                       "\n"
                                       "")
        self.accNumLabel.setObjectName("accNumLabel")
        self.accNumValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.accNumValue.setGeometry(QtCore.QRect(240, 80, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accNumValue.sizePolicy().hasHeightForWidth())
        self.accNumValue.setSizePolicy(sizePolicy)
        self.accNumValue.setMinimumSize(QtCore.QSize(170, 0))
        self.accNumValue.setStyleSheet("border-width:0px;\n"
                                       "border-color: rgb(5, 85, 82);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(245, 247, 250);\n"
                                       "padding-left:20px;\n"
                                       "")
        self.accNumValue.setObjectName("accNumValue")
        self.refNumLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.refNumLabel.setGeometry(QtCore.QRect(160, 50, 81, 21))
        self.refNumLabel.setStyleSheet("border-width:0px;\n"
                                       "border-color: rgb(5, 85, 82);\n"
                                       "border-radius:0px;\n"
                                       "background-color: rgb(202, 205, 210);\n"
                                       "\n"
                                       "")
        self.refNumLabel.setObjectName("refNumLabel")
        self.divider1 = QtWidgets.QWidget(self.cancelOrderWidget)
        self.divider1.setGeometry(QtCore.QRect(130, 20, 20, 81))
        self.divider1.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider1.setObjectName("divider1")
        self.divider2 = QtWidgets.QWidget(self.cancelOrderWidget)
        self.divider2.setGeometry(QtCore.QRect(420, 20, 20, 81))
        self.divider2.setStyleSheet("border-width : 0px;\n"
                                    "border-right-width : 2px;\n"
                                    "border-color: rgb(202, 205, 210);")
        self.divider2.setObjectName("divider2")
        self.orderDateValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.orderDateValue.setGeometry(QtCore.QRect(530, 20, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderDateValue.sizePolicy().hasHeightForWidth())
        self.orderDateValue.setSizePolicy(sizePolicy)
        self.orderDateValue.setMinimumSize(QtCore.QSize(170, 0))
        self.orderDateValue.setStyleSheet("border-width:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "padding-left:20px;\n"
                                          "")
        self.orderDateValue.setObjectName("orderDateValue")
        self.deliverDateLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.deliverDateLabel.setGeometry(QtCore.QRect(450, 50, 81, 21))
        self.deliverDateLabel.setStyleSheet("border-width:0px;\n"
                                            "border-color: rgb(5, 85, 82);\n"
                                            "border-radius:0px;\n"
                                            "background-color: rgb(202, 205, 210);\n"
                                            "\n"
                                            "")
        self.deliverDateLabel.setObjectName("deliverDateLabel")
        self.priceLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.priceLabel.setGeometry(QtCore.QRect(450, 80, 81, 21))
        self.priceLabel.setStyleSheet("border-width:0px;\n"
                                      "border-color: rgb(5, 85, 82);\n"
                                      "border-radius:0px;\n"
                                      "background-color: rgb(202, 205, 210);\n"
                                      "\n"
                                      "")
        self.priceLabel.setObjectName("priceLabel")
        self.priceValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.priceValue.setGeometry(QtCore.QRect(530, 80, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceValue.sizePolicy().hasHeightForWidth())
        self.priceValue.setSizePolicy(sizePolicy)
        self.priceValue.setMinimumSize(QtCore.QSize(170, 0))
        self.priceValue.setStyleSheet("border-width:0px;\n"
                                      "border-color: rgb(5, 85, 82);\n"
                                      "border-radius:0px;\n"
                                      "background-color: rgb(245, 247, 250);\n"
                                      "padding-left:20px;\n"
                                      "")
        self.priceValue.setObjectName("priceValue")
        self.orderDateLabel = QtWidgets.QLabel(self.cancelOrderWidget)
        self.orderDateLabel.setGeometry(QtCore.QRect(450, 20, 81, 21))
        self.orderDateLabel.setStyleSheet("border-width:0px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(202, 205, 210);\n"
                                          "\n"
                                          "")
        self.orderDateLabel.setObjectName("orderDateLabel")
        self.deliverDateValue = QtWidgets.QLabel(self.cancelOrderWidget)
        self.deliverDateValue.setGeometry(QtCore.QRect(530, 50, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deliverDateValue.sizePolicy().hasHeightForWidth())
        self.deliverDateValue.setSizePolicy(sizePolicy)
        self.deliverDateValue.setMinimumSize(QtCore.QSize(170, 0))
        self.deliverDateValue.setStyleSheet("border-width:0px;\n"
                                            "border-color: rgb(5, 85, 82);\n"
                                            "border-radius:0px;\n"
                                            "background-color: rgb(245, 247, 250);\n"
                                            "padding-left:20px;\n"
                                            "")
        self.deliverDateValue.setObjectName("deliverDateValue")
        self.cancelBtn = QtWidgets.QPushButton(self.cancelOrderWidget)
        self.cancelBtn.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.cancelBtn.setStyleSheet("border-width:0px;\n"
                                     "color: rgb(4, 85, 80);\n"
                                     "border-style : solid;\n"
                                     "background-color: rgb(202, 205, 210);\n"
                                     "border-bottom-width : 2px;\n"
                                     "border-color: rgb(5, 85, 82);\n"
                                     "border-radius:0px;\n"
                                     "font-weight : 500;\n"
                                     "font-size: 9pt;\n"
                                     "\n"
                                     "\n"
                                     "")
        self.cancelBtn.setObjectName("cancelBtn")
        self.verticalLayout.addWidget(self.cancelOrderWidget)


        #set label values
        payment = "online" if order.payment_method == 0 else "cash"

        self.paymentLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Payment : </span></p></body></html>")
        self.refNumValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.reference_number}</span></p></body></html>")
        self.paymentValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{payment}</span></p></body></html>")
        self.accNumLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Acc Number</span></p></body></html>")
        self.accNumValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.account_number}</span></p></body></html>")
        self.refNumLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Ref Number</span></p></body></html>")
        self.orderDateValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.order_date}</span></p></body></html>")
        self.deliverDateLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Deliver Date</span></p></body></html>")
        self.priceLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Price : </span></p></body></html>")
        self.priceValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.getPrice()}</span></p></body></html>")
        self.orderDateLabel.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Order Date</span></p></body></html>")
        self.deliverDateValue.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.deliver_date}</span></p></body></html>")
        self.cancelBtn.setText("Cancel")


        #connect buttons
        self.cancelBtn.clicked.connect( partial(cancel, window, self, order  ) )

        #add widget to list
        self.ordersList.append(self.cancelOrderWidget)





    def addLabelOrderWidget(self, window : QtWidgets.QMainWindow, order : Order, labelValue : str):


        self.deliveredOrderWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.deliveredOrderWidget_2.setMinimumSize(QtCore.QSize(0, 120))
        self.deliveredOrderWidget_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.deliveredOrderWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "border-style : solid;\n"
                                                  "border-bottom-width : 2px;\n"
                                                  "border-color: rgb(51, 165, 24);")
        self.deliveredOrderWidget_2.setObjectName("deliveredOrderWidget_2")
        self.paymentLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.paymentLabel_2.setGeometry(QtCore.QRect(160, 20, 81, 21))
        self.paymentLabel_2.setStyleSheet("border-width:0px;\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(202, 205, 210);\n"
                                          "\n"
                                          "")
        self.paymentLabel_2.setObjectName("paymentLabel_2")
        self.refNumValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.refNumValue_2.setGeometry(QtCore.QRect(240, 50, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refNumValue_2.sizePolicy().hasHeightForWidth())
        self.refNumValue_2.setSizePolicy(sizePolicy)
        self.refNumValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.refNumValue_2.setStyleSheet("border-width:0px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(245, 247, 250);\n"
                                         "padding-left:20px;\n"
                                         "")
        self.refNumValue_2.setObjectName("refNumValue_2")
        self.paymentValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.paymentValue_2.setGeometry(QtCore.QRect(240, 20, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paymentValue_2.sizePolicy().hasHeightForWidth())
        self.paymentValue_2.setSizePolicy(sizePolicy)
        self.paymentValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.paymentValue_2.setStyleSheet("border-width:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "border-color: rgb(5, 85, 82);\n"
                                          "border-radius:0px;\n"
                                          "background-color: rgb(245, 247, 250);\n"
                                          "padding-left:20px;\n"
                                          "")
        self.paymentValue_2.setObjectName("paymentValue_2")
        self.accNumLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.accNumLabel_2.setGeometry(QtCore.QRect(160, 80, 81, 21))
        self.accNumLabel_2.setStyleSheet("border-width:0px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(202, 205, 210);\n"
                                         "\n"
                                         "")
        self.accNumLabel_2.setObjectName("accNumLabel_2")
        self.accNumValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.accNumValue_2.setGeometry(QtCore.QRect(240, 80, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accNumValue_2.sizePolicy().hasHeightForWidth())
        self.accNumValue_2.setSizePolicy(sizePolicy)
        self.accNumValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.accNumValue_2.setStyleSheet("border-width:0px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(245, 247, 250);\n"
                                         "padding-left:20px;\n"
                                         "")
        self.accNumValue_2.setObjectName("accNumValue_2")
        self.refNumLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.refNumLabel_2.setGeometry(QtCore.QRect(160, 50, 81, 21))
        self.refNumLabel_2.setStyleSheet("border-width:0px;\n"
                                         "border-color: rgb(5, 85, 82);\n"
                                         "border-radius:0px;\n"
                                         "background-color: rgb(202, 205, 210);\n"
                                         "\n"
                                         "")
        self.refNumLabel_2.setObjectName("refNumLabel_2")
        self.divider1_2 = QtWidgets.QWidget(self.deliveredOrderWidget_2)
        self.divider1_2.setGeometry(QtCore.QRect(130, 20, 20, 81))
        self.divider1_2.setStyleSheet("border-width : 0px;\n"
                                      "border-right-width : 2px;\n"
                                      "border-color: rgb(202, 205, 210);")
        self.divider1_2.setObjectName("divider1_2")
        self.divider2_2 = QtWidgets.QWidget(self.deliveredOrderWidget_2)
        self.divider2_2.setGeometry(QtCore.QRect(420, 20, 20, 81))
        self.divider2_2.setStyleSheet("border-width : 0px;\n"
                                      "border-right-width : 2px;\n"
                                      "border-color: rgb(202, 205, 210);")
        self.divider2_2.setObjectName("divider2_2")
        self.orderDateValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.orderDateValue_2.setGeometry(QtCore.QRect(530, 20, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderDateValue_2.sizePolicy().hasHeightForWidth())
        self.orderDateValue_2.setSizePolicy(sizePolicy)
        self.orderDateValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.orderDateValue_2.setStyleSheet("border-width:0px;\n"
                                            "background-color: rgb(245, 247, 250);\n"
                                            "border-color: rgb(5, 85, 82);\n"
                                            "border-radius:0px;\n"
                                            "background-color: rgb(245, 247, 250);\n"
                                            "padding-left:20px;\n"
                                            "")
        self.orderDateValue_2.setObjectName("orderDateValue_2")
        self.deliverDateLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.deliverDateLabel_2.setGeometry(QtCore.QRect(450, 50, 81, 21))
        self.deliverDateLabel_2.setStyleSheet("border-width:0px;\n"
                                              "border-color: rgb(5, 85, 82);\n"
                                              "border-radius:0px;\n"
                                              "background-color: rgb(202, 205, 210);\n"
                                              "\n"
                                              "")
        self.deliverDateLabel_2.setObjectName("deliverDateLabel_2")
        self.priceLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.priceLabel_2.setGeometry(QtCore.QRect(450, 80, 81, 21))
        self.priceLabel_2.setStyleSheet("border-width:0px;\n"
                                        "border-color: rgb(5, 85, 82);\n"
                                        "border-radius:0px;\n"
                                        "background-color: rgb(202, 205, 210);\n"
                                        "\n"
                                        "")
        self.priceLabel_2.setObjectName("priceLabel_2")
        self.priceValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.priceValue_2.setGeometry(QtCore.QRect(530, 80, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceValue_2.sizePolicy().hasHeightForWidth())
        self.priceValue_2.setSizePolicy(sizePolicy)
        self.priceValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.priceValue_2.setStyleSheet("border-width:0px;\n"
                                        "border-color: rgb(5, 85, 82);\n"
                                        "border-radius:0px;\n"
                                        "background-color: rgb(245, 247, 250);\n"
                                        "padding-left:20px;\n"
                                        "")
        self.priceValue_2.setObjectName("priceValue_2")
        self.orderDateLabel_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.orderDateLabel_2.setGeometry(QtCore.QRect(450, 20, 81, 21))
        self.orderDateLabel_2.setStyleSheet("border-width:0px;\n"
                                            "border-color: rgb(5, 85, 82);\n"
                                            "border-radius:0px;\n"
                                            "background-color: rgb(202, 205, 210);\n"
                                            "\n"
                                            "")
        self.orderDateLabel_2.setObjectName("orderDateLabel_2")
        self.deliverDateValue_2 = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.deliverDateValue_2.setGeometry(QtCore.QRect(530, 50, 170, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deliverDateValue_2.sizePolicy().hasHeightForWidth())
        self.deliverDateValue_2.setSizePolicy(sizePolicy)
        self.deliverDateValue_2.setMinimumSize(QtCore.QSize(170, 0))
        self.deliverDateValue_2.setStyleSheet("border-width:0px;\n"
                                              "border-color: rgb(5, 85, 82);\n"
                                              "border-radius:0px;\n"
                                              "background-color: rgb(245, 247, 250);\n"
                                              "padding-left:20px;\n"
                                              "")
        self.deliverDateValue_2.setObjectName("deliverDateValue_2")
        self.deliveredLabel = QtWidgets.QLabel(self.deliveredOrderWidget_2)
        self.deliveredLabel.setGeometry(QtCore.QRect(20, 20, 101, 41))
        self.deliveredLabel.setStyleSheet("border-width:0px;\n"
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
        self.deliveredLabel.setObjectName("deliveredLabel")
        self.verticalLayout.addWidget(self.deliveredOrderWidget_2)

        # set label values
        payment = "online" if order.payment_method == 0 else "cash"

        self.paymentLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Payment : </span></p></body></html>")
        self.refNumValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.reference_number}</span></p></body></html>")
        self.paymentValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{payment}</span></p></body></html>")
        self.accNumLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Acc Number</span></p></body></html>")
        self.accNumValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.account_number}</span></p></body></html>")
        self.refNumLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Ref Number</span></p></body></html>")
        self.orderDateValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.deliver_date}</span></p></body></html>")
        self.deliverDateLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Deliver Date</span></p></body></html>")
        self.priceLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Price : </span></p></body></html>")
        self.priceValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.getPrice()}</span></p></body></html>")
        self.orderDateLabel_2.setText("<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">Order Date</span></p></body></html>")
        self.deliverDateValue_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" color:#055552;\">{order.deliver_date}</span></p></body></html>")
        self.deliveredLabel.setText(f"<html><head/><body><p align=\"center\">{labelValue}</p></body></html>")




        #add order to list
        self.ordersList.append(self.deliveredOrderWidget_2)






    def setupUi(self, MainWindow):

        self.ordersList = []

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
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 30, 771, 501))
        self.scrollArea_2.setStyleSheet("border-radius : 0px;\n"
                                        "border-width : 0px;\n"
                                        "background-color: rgb(245, 247, 250);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 771, 501))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.historyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.historyBtn.setGeometry(QtCore.QRect(850, 230, 91, 50))
        self.historyBtn.setStyleSheet("border-color: rgb(4, 84, 83);\n"
                                      "background-color: rgb(245, 247, 250);\n"
                                      "border-style : solid;\n"
                                      "border-bottom-width : 2px;\n"
                                      "border-right-width : 2px;\n"
                                      "border-bottom-right-radius: 20px;\n"
                                      "box-shadow: 10px 10px 5px -5px #666;\n"
                                      "color: rgb(4, 84, 83);\n"
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

        self.retranslateUi(MainWindow)

        # ////////////////run init////////////////////
        init(MainWindow, self)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):


        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.historyBtn.setText(_translate("MainWindow", "HISTORY"))
        self.logoutBtn.setText(_translate("MainWindow", "LOG OUT"))
        self.accountBtn.setText(_translate("MainWindow", "ACCOUNT"))
        self.orderBtn.setText(_translate("MainWindow", "ORDER"))
        self.backBtn.setText(_translate("MainWindow", "BACK"))
        self.mainTitle.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.mainTitle.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#055553;\">{Restaurant.Name()}</span></p></body></html>"))
        self.windowTitle.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#33a415;\">Orders History</span></p></body></html>"))
        self.cartBtn.setText(_translate("MainWindow", "CART"))








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())










