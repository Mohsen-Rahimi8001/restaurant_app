from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from functools import partial
from Window import Routing


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(696, 502)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 671, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainVLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVLayout.setObjectName("mainVLayout")
        self.lblTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblTitle.setSizeIncrement(QtCore.QSize(-31072, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setTextFormat(QtCore.Qt.AutoText)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.mainVLayout.addWidget(self.lblTitle)
        self.btnLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnLogin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.btnLogin.setFont(font)
        self.btnLogin.setIconSize(QtCore.QSize(16, 16))
        self.btnLogin.setCheckable(False)
        self.btnLogin.setAutoDefault(False)
        self.btnLogin.setDefault(False)
        self.btnLogin.setFlat(False)
        self.btnLogin.setObjectName("btnLogin")

        blogin = partial(Routing.Redirect, HomeWindow, "login")
        self.btnLogin.clicked.connect(blogin)


        self.mainVLayout.addWidget(self.btnLogin)
        self.btnSignUp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSignUp.sizePolicy().hasHeightForWidth())
        self.btnSignUp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setObjectName("btnSignUp")

        bound_signup = partial(Routing.Redirect, HomeWindow, "signup")
        self.btnSignUp.clicked.connect(bound_signup)

        self.mainVLayout.addWidget(self.btnSignUp)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)
    
    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        self.lblTitle.setText(_translate("HomeWindow", "Home Page"))
        self.btnLogin.setText(_translate("HomeWindow", "Login"))
        self.btnSignUp.setText(_translate("HomeWindow", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())



