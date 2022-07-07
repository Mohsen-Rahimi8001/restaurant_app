from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Message import Message
from Controllers.AuthenticationController import Auth
from Lib.SpellCorrecting import SpellCorrecting
from Window import Routing
import datetime as dt


def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """Checks if the user is logged in and has the admin credentials."""
    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'login')
        Routing.ClearStack()


def setUpInitInformation(ui: 'Ui_MainWindow'):
    """Sets up the initial information for the form."""
    # get the messages
    messages = Message.GetAll()
    
    # put the messages in the chat text edit
    for message in messages:
        addMessage(ui, message.admin_email, message.datetime, message.message)


def addMessage(ui : 'Ui_MainWindow', email : str, datetime : str, text : str):
    """Adds a message to the Chat room"""
    
    text = f"[{email}_{datetime}]: {text}\n\n"
    ui.tEditChats.insertPlainText(text)


# ////////////////////////////////EVENTS////////////////////////////
def sendMessage(ui: "Ui_MainWindow"):
    """send the message in the chat room and save it in the database"""
    
    # get the message
    message = ui.lEditMessage.text()
    
    # get the admin email
    admin_email = Auth.GetUser().email
    
    # get the datetime
    datetime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # create the message in the database
    Message.Create({
        'message': message,
        'admin_email': admin_email,
        'datetime': datetime
    })

    # clear the message text edit
    ui.lEditMessage.setText("")

    # push the message to the chat room
    addMessage(ui, admin_email, datetime, message)


def enableSpellCorrecting(ui : 'Ui_MainWindow'):
    """connect the lEditMessage to the spell correcting function"""
    if ui.chBoxSpellCorrecting.isChecked():
        ui.lEditMessage.textChanged.connect(lambda: SpellCorrecting.KeyPressHandler(ui.lEditMessage))
    else:
        ui.lEditMessage.textChanged.disconnect()


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
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.lEditMessage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditMessage.setObjectName("lEditMessage")
        self.lEditMessage.returnPressed.connect(lambda:sendMessage(self))
        self.gridLayout.addWidget(self.lEditMessage, 2, 0, 1, 1)
        
        self.chBoxSpellCorrecting = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        self.chBoxSpellCorrecting.setFont(font)
        self.chBoxSpellCorrecting.setObjectName("chBoxSpellCorrecting")
        self.chBoxSpellCorrecting.toggled.connect(lambda:enableSpellCorrecting(self))
        self.gridLayout.addWidget(self.chBoxSpellCorrecting, 2, 1, 1, 1)
        
        self.btnSend = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnSend.setFont(font)
        self.btnSend.setObjectName("btnSend")
        self.btnSend.clicked.connect(lambda: sendMessage(self))
        self.gridLayout.addWidget(self.btnSend, 2, 2, 1, 1)

        self.btnBack = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda:Routing.RedirectBack(MainWindow))
        self.gridLayout.addWidget(self.btnBack, 3, 0, 1, 3)

        self.tEditChats = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.tEditChats.setObjectName("tEditChats")
        self.tEditChats.setReadOnly(True)
        self.gridLayout.addWidget(self.tEditChats, 1, 0, 1, 3)
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow : 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chBoxSpellCorrecting.setText(_translate("MainWindow", "Assistant"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.lblTitle.setText(_translate("MainWindow", "Chat Room"))
        self.btnBack.setText(_translate("MainWindow", "Back"))

        checkForCredentials(MainWindow)
        setUpInitInformation(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
