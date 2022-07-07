from PyQt5 import QtCore, QtGui, QtWidgets
from Window import Routing
from Controllers.AuthenticationController import Auth
from Controllers.Admin.GiftCardController import GiftCardController
from Lib.Messages import Messages
from Models.GiftCard import GiftCard
from functools import partial



def checkForCredentials(window: "QtWidgets.QMainWindow"):
    """Checks if the user is logged in and has the admin credentials."""
    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'login')
        Routing.ClearStack()        


def setUpInitInformation(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """fetch the giftcards from database and fill in in the table"""

    # get all giftcards
    giftcards = GiftCard.GetAll()

    i = -1

    # put the date in the table
    for giftcard in giftcards:
        
        i += 1

        if giftcard.sent:
            i -= 1
            continue

        ui.tableGiftCards.setRowCount(i + 1)

        # create send button
        sendIcon = QtGui.QIcon(r".\Resources\Images\send_icon.png")
        btnSend = QtWidgets.QPushButton()
        btnSend.setIcon(sendIcon)
        btnSend.setIconSize(QtCore.QSize(20, 20))
        sendSignal = partial(sendGiftcard, giftcard.id, window)

        # create a delete button
        deleteIcon = QtGui.QIcon(r".\Resources\Images\delete_icon.png")
        btnDelete = QtWidgets.QPushButton()
        btnDelete.setIcon(deleteIcon)
        btnDelete.setIconSize(QtCore.QSize(20, 20))
        deleteSignal = partial(deleteGiftcard, giftcard.id, window)

        ui.tableGiftCards.setItem(i, 0, QtWidgets.QTableWidgetItem(str(giftcard.id)))
        ui.tableGiftCards.setItem(i, 1, QtWidgets.QTableWidgetItem(giftcard.start_date.strftime('%Y-%m-%d')))
        ui.tableGiftCards.setItem(i, 2, QtWidgets.QTableWidgetItem(giftcard.expiration_date.strftime('%Y-%m-%d')))
        ui.tableGiftCards.setItem(i, 3, QtWidgets.QTableWidgetItem(str(giftcard.amount)))
        ui.tableGiftCards.setItem(i, 4, QtWidgets.QTableWidgetItem(str(giftcard.code)))

        # add the delete button to delete column
        ui.tableGiftCards.setCellWidget(i, 5, btnDelete)

        # add the send button to send column
        ui.tableGiftCards.setCellWidget(i, 6, btnSend)

        # connect the delete button to the signal
        btnDelete.clicked.connect(deleteSignal)

        # connect the send button to the signal
        btnSend.clicked.connect(sendSignal)



# ////////////////////////////////EVENTS////////////////////////////
def deleteGiftcard(giftcard_id: int, window: "QtWidgets.QMainWindow"):
    """Deletes a giftcard from the database."""
    
    # delete the giftcard
    GiftCard.Delete(giftcard_id)

    # show a message
    Messages.push(Messages.Type.SUCCESS, "Giftcard deleted successfully.")

    # refresh the page
    Routing.Refresh(window)    


def sendGiftcard(giftCardId:int, window: "QtWidgets.QMainWindow"):
    """Sends the gift card to all users"""
    
    giftCard = GiftCard.Get(giftCardId)

    GiftCardController.SendToAll(giftCard)

    Messages.push(Messages.Type.SUCCESS, "Giftcard sent successfully.")
    
    # refresh the page
    Routing.Refresh(window)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 881, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTItle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTItle.sizePolicy().hasHeightForWidth())
        
        self.lblTItle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTItle.setFont(font)
        self.lblTItle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTItle.setObjectName("lblTItle")
        self.gridLayout.addWidget(self.lblTItle, 0, 0, 1, 1)
        
        self.tableGiftCards = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableGiftCards.sizePolicy().hasHeightForWidth())
        self.tableGiftCards.setSizePolicy(sizePolicy)
        self.tableGiftCards.setObjectName("tableGiftCards")
        self.tableGiftCards.setColumnCount(7)
        self.tableGiftCards.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(4, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(5, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableGiftCards.setHorizontalHeaderItem(6, item)

        # set table row height
        self.tableGiftCards.setRowHeight(0, 30)

        # set table column width
        self.tableGiftCards.setColumnWidth(0, 10) # id
        self.tableGiftCards.setColumnWidth(1, 200) # start date
        self.tableGiftCards.setColumnWidth(2, 200) # expiration date
        self.tableGiftCards.setColumnWidth(3, 100) # amount
        self.tableGiftCards.setColumnWidth(4, 200) # code
        self.tableGiftCards.setColumnWidth(5, 100) # delete
        self.tableGiftCards.setColumnWidth(6, 100) # send

        # set table edit behavior (not editable)
        self.tableGiftCards.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.gridLayout.addWidget(self.tableGiftCards, 1, 0, 1, 1)
        
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setContentsMargins(5, 5, 5, 5)
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

        self.btnSuggest = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnSuggest.setFont(font)
        self.btnSuggest.setObjectName("btnSuggest")
        self.btnSuggest.clicked.connect(GiftCardController.Suggest)
        self.btnHLayout.addWidget(self.btnSuggest)

        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(lambda:Routing.Redirect(MainWindow, "newGiftCard"))
        self.btnHLayout.addWidget(self.btnAdd)
        
        self.gridLayout.addLayout(self.btnHLayout, 2, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTItle.setText(_translate("MainWindow", "Gift Cards"))
        item = self.tableGiftCards.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableGiftCards.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.tableGiftCards.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Expiration Date"))
        item = self.tableGiftCards.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.tableGiftCards.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableGiftCards.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delete"))
        item = self.tableGiftCards.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Send"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnSuggest.setText(_translate("MainWindow", "Suggest"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))

        checkForCredentials(MainWindow)
        setUpInitInformation(self, MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
