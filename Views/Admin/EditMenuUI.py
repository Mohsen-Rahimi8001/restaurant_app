from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Window import Routing, Transfer
from Lib.Messages import Messages
from Models.Menu import Menu
from Models.Food import Food
from functools import partial


MENU: Menu = None

def setMenuObject():
    """This function sets the menu object to the global variable MENU"""
    global MENU

    menuId = Transfer.Get('id')
    MENU = Menu.Get(menuId)


def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """checks if the user is logged in and has the admin credentials"""

    if not Auth.IsUserLoggedIN():
        # go to the landing page
        Routing.Redirect(window, 'landingPage')
        Routing.ClearStack()
        return

    if not Auth.CheckAdminCredentials():
        # logout the user
        Auth.LogOut()
        # go to the landing page
        Routing.Redirect(window, 'landingPage')
        Routing.ClearStack()  # reset the previous window
        return


def setUpInitInformation(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """fill the foods table and the menu table"""

    # fetched all the foods
    foods = Food.GetAll()

    ui.tableFoods.setRowCount(len(foods))

    # set the foods to the food table
    for i, food in enumerate(foods):

        # create add button
        addIcon = QtGui.QIcon(r".\Resources\Images\add_icon.png")
        btnAdd = QtWidgets.QPushButton()
        btnAdd.setIcon(addIcon)
        btnAdd.setIconSize(QtCore.QSize(20, 20))
        addSignal = partial(addFood, food, ui, window)

        # create an icon of the food image
        foodIcon = QtGui.QIcon(food.image)

        ui.tableFoods.setItem(i, 0, QtWidgets.QTableWidgetItem(str(food.id)))
        ui.tableFoods.setItem(i, 1, QtWidgets.QTableWidgetItem(foodIcon, "", QtCore.Qt.DecorationRole))
        ui.tableFoods.setItem(i, 2, QtWidgets.QTableWidgetItem(food.title))
        ui.tableFoods.setItem(i, 3, QtWidgets.QTableWidgetItem(str(food.stock)))
        ui.tableFoods.setItem(i, 4, QtWidgets.QTableWidgetItem(str(food.fixed_price)))
        ui.tableFoods.setItem(i, 5, QtWidgets.QTableWidgetItem(str(food.sale_price)))

        # add the add button to add column
        ui.tableFoods.setCellWidget(i, 6, btnAdd)

        # connect the add button to the add signal
        btnAdd.clicked.connect(addSignal)


    # fetched foods in the menu and set them to the menu table
    foodsInMenu = MENU.getFoods()

    ui.tableMenuFoods.setRowCount(len(foodsInMenu))

    for i, food in enumerate(foodsInMenu):
            
        # create remove button
        removeIcon = QtGui.QIcon(r".\Resources\Images\delete_icon.png")
        btnRemove = QtWidgets.QPushButton()
        btnRemove.setIcon(removeIcon)
        btnRemove.setIconSize(QtCore.QSize(20, 20))
        removeSignal = partial(removeFood, food, ui, window)

        # create an icon of the food image
        foodIcon = QtGui.QIcon(food.image)

        ui.tableMenuFoods.setItem(i, 0, QtWidgets.QTableWidgetItem(str(food.id)))
        ui.tableMenuFoods.setItem(i, 1, QtWidgets.QTableWidgetItem(foodIcon, "", QtCore.Qt.DecorationRole))
        ui.tableMenuFoods.setItem(i, 2, QtWidgets.QTableWidgetItem(food.title))
        ui.tableMenuFoods.setItem(i, 3, QtWidgets.QTableWidgetItem(str(food.stock)))
        ui.tableMenuFoods.setItem(i, 4, QtWidgets.QTableWidgetItem(str(food.fixed_price)))
        ui.tableMenuFoods.setItem(i, 5, QtWidgets.QTableWidgetItem(str(food.sale_price)))

        # add the remove button to remove column
        ui.tableMenuFoods.setCellWidget(i, 6, btnRemove)

        # connect the remove button to the remove signal
        btnRemove.clicked.connect(removeSignal)

    # add the name of the menu
    ui.lEditMenuTitle.setText(MENU.title)


# /////////////////////////////EVENTS////////////////////////////
def addFood(food: Food, ui: 'Ui_MainWindow', window: "QtWidgets.QMainWindow"):
    """adds a food to the menu"""

    if food.id not in MENU.foods:
        # add the food to the menu
        MENU.addFood(food)
    else:
        # show error message
        Messages.push(Messages.Type.ERROR, "Food already exists in menu")
        Messages.show()
        return
        
    # update the menu table
    refreshPage(ui, window)

    # show a message
    Messages.push(Messages.Type.SUCCESS, "Food added to menu")
    Messages.show()


def removeFood(food: Food, ui: 'Ui_MainWindow', window: "QtWidgets.QMainWindow"):
    """removes a food from the menu"""

    # remove the food from the menu
    MENU.removeFood(food)

    # update the menu table
    refreshPage(ui, window)

    # show a message
    Messages.push(Messages.Type.SUCCESS ,"Food removed from the menu")
    Messages.show()


def refreshPage(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """refreshes the page"""

    # clear two tables
    ui.tableFoods.setRowCount(0)
    ui.tableMenuFoods.setRowCount(0)

    setUpInitInformation(ui, window)        



def saveChanges(ui: "Ui_MainWindow"):
    """saves the changes (just the new name)"""

    # get the new name
    newTitle = ui.lEditMenuTitle.text()

    # update the menu
    Menu.Update(MENU.id, {'title' : newTitle})
    
    # show a message
    Messages.push(Messages.Type.SUCCESS, "Menu updated")
    Messages.show()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 832)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 811, 781))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)
        
        self.lblMenuTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblMenuTitle.setFont(font)
        self.lblMenuTitle.setObjectName("lblMenuTitle")
        self.gridLayout.addWidget(self.lblMenuTitle, 3, 0, 1, 1)
        
        self.lEditMenuTitle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditMenuTitle.setObjectName("lEditMenuTitle")
        self.gridLayout.addWidget(self.lEditMenuTitle, 3, 1, 1, 1)
        
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setContentsMargins(5, 5, 5, 5)
        self.btnHLayout.setSpacing(10)
        self.btnHLayout.setObjectName("btnHLayout")
        
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda:Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
                
        self.btnChange = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnChange.setFont(font)
        self.btnChange.setObjectName("btnChange")
        self.btnChange.clicked.connect(lambda:saveChanges(self))
        self.btnHLayout.addWidget(self.btnChange)
        
        self.gridLayout.addLayout(self.btnHLayout, 4, 0, 1, 2)
        
        self.tableMenuFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableMenuFoods.sizePolicy().hasHeightForWidth())
        self.tableMenuFoods.setSizePolicy(sizePolicy)
        self.tableMenuFoods.setObjectName("tableMenuFoods")
        self.tableMenuFoods.setColumnCount(7)
        self.tableMenuFoods.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenuFoods.setHorizontalHeaderItem(6, item)
        
        self.gridLayout.addWidget(self.tableMenuFoods, 2, 0, 1, 2)
        
        self.tableFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableFoods.sizePolicy().hasHeightForWidth())
        self.tableFoods.setSizePolicy(sizePolicy)
        self.tableFoods.setObjectName("tableFoods")
        self.tableFoods.setColumnCount(7)
        self.tableFoods.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(2, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(4, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(6, item)
        
        self.gridLayout.addWidget(self.tableFoods, 1, 0, 1, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Edit Menu"))
        self.lblMenuTitle.setText(_translate("MainWindow", "Menu New Title: "))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        item = self.tableMenuFoods.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableMenuFoods.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Image"))
        item = self.tableMenuFoods.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableMenuFoods.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.tableMenuFoods.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fixed Price"))
        item = self.tableMenuFoods.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sale Price"))
        item = self.tableMenuFoods.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Delete"))
        item = self.tableFoods.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableFoods.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Image"))
        item = self.tableFoods.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableFoods.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock"))
        item = self.tableFoods.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fixed Price"))
        item = self.tableFoods.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sale Price"))
        item = self.tableFoods.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Add"))

        # this function sets the MENU every time the page is loaded
        setMenuObject()
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
