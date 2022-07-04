from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Models.Restaurant import Restaurant
from Window import Routing


# ////////////////////////////EVENTS////////////////////////////
def setInitInformation(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """sets admin information and restaurant information in the home page"""

    # check if the user is admin
    if not Auth.CheckAdminCredentials():
        # logout the user
        Auth.LogOut()
        # redirect to login page
        Routing.Redirect(window, 'login')
        Routing.ClearStack() # reset previous window

    # get the admin information
    admin = Auth.GetUser()
    
    # set admin information
    # set profile image
    setProfileImage(ui, admin.image)
    setAdminName(ui, admin.first_name + " " + admin.last_name)
    setAdminEmail(ui, admin.email)
    setAdminPhone(ui, admin.phone_number)

    # get restaurant information
    restaurant = Restaurant.LoadFromJson()

    # set restaurant information
    setRestaurantName(ui, restaurant.restaurantName)
    setRestaurantPhone(ui, restaurant.phone)
    setRestaurantRegion(ui, restaurant.region)
    setRestaurantAddress(ui, restaurant.address)


def setProfileImage(ui: "Ui_MainWindow", image:str):
    """
    sets the profile image
    image: directory of the image
    """
    ui.lblProf.setPixmap(QtGui.QPixmap(image))
    ui.lblProf.setScaledContents(True)

    # resize the image
    ui.lblProf.setFixedSize(150, 120)

    ui.lblProf.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    ui.lblProf.setAlignment(QtCore.Qt.AlignCenter)
    ui.lblProf.setObjectName("lblProf")


def setAdminName(ui: "Ui_MainWindow", name:str):
    """
    sets the admin name
    name: name of the admin
    """
    ui.lblAFullName.setText(ui.lblAFullName.text() + name)


def setAdminEmail(ui: "Ui_MainWindow", email:str):
    """
    sets the admin email
    email: email of the admin
    """
    ui.lblEmail.setText(ui.lblEmail.text() + email)


def setAdminPhone(ui: "Ui_MainWindow", phone:str):
    """
    sets the admin phone
    phone: phone of the admin
    """
    ui.lblPhoneNumber.setText(ui.lblPhoneNumber.text() + phone + '\n\n')


def setRestaurantName(ui: "Ui_MainWindow", name:str):
    """
    sets the restaurant name
    name: name of the restaurant
    """
    ui.lblRestaurantName.setText(ui.lblRestaurantName.text() + name)


def setRestaurantPhone(ui: "Ui_MainWindow", phone:str):
    """
    sets the restaurant phone
    phone: phone of the restaurant
    """
    ui.lblRestPhone.setText(ui.lblRestPhone.text() + phone)


def setRestaurantRegion(ui: "Ui_MainWindow", region:str):
    """
    sets the restaurant region
    region: region of the restaurant
    """
    ui.lblRestRegion.setText(ui.lblRestRegion.text() + region)


def setRestaurantAddress(ui: "Ui_MainWindow", address:str):
    """
    sets the restaurant address
    address: address of the restaurant
    """
    ui.lblRestAddress.setText(ui.lblRestAddress.text() + address)


def goToFoodsPage(window: 'QtWidgets.QMainWindow'):
    """redirects to foods page"""
    Routing.Redirect(window, 'foods')


def goToMenusPage(window: 'QtWidgets.QMainWindow'):
    """redirects to menus page"""
    Routing.Redirect(window, 'menus')


def goToGiftCards(window: 'QtWidgets.QMainWindow'):
    """redirects to gift cards page"""
    Routing.Redirect(window, 'giftCards')


def gotoOrders(window: 'QtWidgets.QMainWindow'):
    """redirects to orders page"""
    Routing.Redirect(window, 'orders')


def goToStatus(window: 'QtWidgets.QMainWindow'):
    """redirects to status page"""
    Routing.Redirect(window, 'status')

def goToEditRestaurant(window: 'QtWidgets.QMainWindow'):
    """redirects to edit restaurant page"""
    Routing.Redirect(window, 'editRestaurant')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow:'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 720, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.btnFoods = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnFoods.setFont(font)
        self.btnFoods.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnFoods.setObjectName("btnFoods")
        self.verticalLayout.addWidget(self.btnFoods)
        self.btnFoods.clicked.connect(lambda: goToFoodsPage(MainWindow))

        self.btnMenus = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnMenus.setFont(font)
        self.btnMenus.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnMenus.setObjectName("btnMenus")
        self.verticalLayout.addWidget(self.btnMenus)
        self.btnMenus.clicked.connect(lambda: goToMenusPage(MainWindow))
        
        self.btnGiftCards = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnGiftCards.setFont(font)
        self.btnGiftCards.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnGiftCards.setObjectName("btnGiftCards")
        self.verticalLayout.addWidget(self.btnGiftCards)
        self.btnGiftCards.clicked.connect(lambda: goToGiftCards(MainWindow))
        
        self.btnOrders = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnOrders.setFont(font)
        self.btnOrders.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnOrders.setObjectName("btnOrders")
        self.verticalLayout.addWidget(self.btnOrders)
        self.btnOrders.clicked.connect(lambda: gotoOrders(MainWindow))
        
        self.btnEconomic = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnEconomic.setFont(font)
        self.btnEconomic.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnEconomic.setObjectName("btnEconomic")
        self.verticalLayout.addWidget(self.btnEconomic)
        self.btnEconomic.clicked.connect(lambda: goToStatus(MainWindow))
        
        self.btnEditRestaurantInfo = QtWidgets.QPushButton(self.gridLayoutWidget)
        font.setPointSize(9)
        self.btnEditRestaurantInfo.setFont(font)
        self.btnEditRestaurantInfo.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.btnEditRestaurantInfo.setObjectName("btnEditRestaurantInfo")
        self.verticalLayout.addWidget(self.btnEditRestaurantInfo)
        self.btnEditRestaurantInfo.clicked.connect(lambda: goToEditRestaurant(MainWindow))
        
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 6, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.lblRestInfoTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.lblRestInfoTitle.setFont(font)
        self.lblRestInfoTitle.setObjectName("lblRestInfoTitle")
        self.verticalLayout_3.addWidget(self.lblRestInfoTitle)
        
        self.lblRestaurantName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRestaurantName.setFont(font)
        self.lblRestaurantName.setObjectName("lblRestaurantName")
        self.verticalLayout_3.addWidget(self.lblRestaurantName)
        
        self.lblRestPhone = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRestPhone.setFont(font)
        self.lblRestPhone.setObjectName("lblRestPhone")
        self.verticalLayout_3.addWidget(self.lblRestPhone)
        
        self.lblRestRegion = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRestRegion.setFont(font)
        self.lblRestRegion.setObjectName("lblRestRegion")
        self.verticalLayout_3.addWidget(self.lblRestRegion)
        
        self.lblRestAddress = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblRestAddress.setFont(font)
        self.lblRestAddress.setObjectName("lblRestAddress")
        self.verticalLayout_3.addWidget(self.lblRestAddress)

        # create a verticalSpacer (w, h)
        label = QtWidgets.QLabel()
        self.verticalLayout_3.addWidget(label)
        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(verticalSpacer)

        self.gridLayout.addLayout(self.verticalLayout_3, 4, 0, 3, 1)
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.lblAdminInfoTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(15)
        self.lblAdminInfoTitle.setFont(font)
        self.lblAdminInfoTitle.setObjectName("lblAdminInfoTitle")
        self.verticalLayout_2.addWidget(self.lblAdminInfoTitle)
        
        self.lblProf = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblProf.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProf.setObjectName("lblProf")
        self.verticalLayout_2.addWidget(self.lblProf)
        
        self.lblAFullName = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblAFullName.setFont(font)
        self.lblAFullName.setObjectName("lblAFullName")
        self.verticalLayout_2.addWidget(self.lblAFullName)
        
        self.lblEmail = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblEmail.setFont(font)
        self.lblEmail.setObjectName("lblEmail")
        self.verticalLayout_2.addWidget(self.lblEmail)
        
        self.lblPhoneNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.lblPhoneNumber.setFont(font)
        self.lblPhoneNumber.setObjectName("lblPhoneNumber")
        self.verticalLayout_2.addWidget(self.lblPhoneNumber)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 3, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow:'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Home"))
        self.btnFoods.setText(_translate("MainWindow", "Foods"))
        self.btnMenus.setText(_translate("MainWindow", "Menus"))
        self.btnGiftCards.setText(_translate("MainWindow", "Gift Cards"))
        self.btnOrders.setText(_translate("MainWindow", "Orders"))
        self.btnEconomic.setText(_translate("MainWindow", "Economic Situation"))
        self.btnEditRestaurantInfo.setText(_translate("MainWindow", "Edit Restaurant Info"))
        self.lblRestInfoTitle.setText(_translate("MainWindow", "Restaurant Info"))
        self.lblRestaurantName.setText(_translate("MainWindow", "Name: "))
        self.lblRestPhone.setText(_translate("MainWindow", "Phone Number: "))
        self.lblRestRegion.setText(_translate("MainWindow", "Region: "))
        self.lblRestAddress.setText(_translate("MainWindow", "Address: "))
        self.lblAdminInfoTitle.setText(_translate("MainWindow", "Admin Info"))
        self.lblProf.setText(_translate("MainWindow", "TextLabel"))
        self.lblAFullName.setText(_translate("MainWindow", "Name:  "))
        self.lblEmail.setText(_translate("MainWindow", "Email: "))
        self.lblPhoneNumber.setText(_translate("MainWindow", "Phone Number: "))
        
        # set up initial information
        setInitInformation(self, MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
