from PyQt5 import QtCore, QtGui, QtWidgets
from Window import Routing
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Models.Food import Food
from Models.Menu import Menu
from functools import partial
import datetime as dt


def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """Check if the user is logged in and has admin access"""
    if not Auth.IsUserLoggedIN():
        Routing.Redirect(window, 'login')
        Routing.ClearStack()
        return
    
    if not Auth.CheckAdminCredentials():
        Auth.LogOut()
        Routing.Redirect(window, 'adminHome')
        Routing.ClearStack()


def setUpInitInformation(ui: 'Ui_MainWindow'):
    """Fetch foods and place them in the table"""

    # Fetch foods
    foods = Food.GetAll()

    # Set up table
    ui.tableFoods.setRowCount(len(foods))

    # Populate table
    for i, food in enumerate(foods):

        # create add button
        addIcon = QtGui.QIcon(r".\Resources\Images\add_icon.png")
        btnAdd = QtWidgets.QPushButton()
        btnAdd.setIcon(addIcon)
        btnAdd.setIconSize(QtCore.QSize(20, 20))
        addSignal = partial(addFood, food, ui)

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


def getFoodIds(ui: "Ui_MainWindow") -> list[int]:
    """Get the food ids from the menu table"""

    # get the number of rows in the menu table
    rowCount = ui.tableMenuFoods.rowCount()

    # get the food ids from the menu table
    foodIds = []
    for i in range(rowCount):
        foodIds.append(int(ui.tableMenuFoods.item(i, 0).text()))

    return foodIds


# ////////////////////////////////EVENTS////////////////////////////
def addFood(food: Food, ui: "Ui_MainWindow"):
    """Add a food to the menu table"""
    
    # check if the food is repetitive
    if food.id in getFoodIds(ui):
        Messages.push(Messages.Type.ERROR, "Food already in menu")
        Messages.show()
        return

    # get the number of rows in the menu table
    rowCount = ui.tableMenuFoods.rowCount()

    # add a row to menu table
    ui.tableMenuFoods.setRowCount(rowCount + 1)

    # create an icon of the food image
    foodIcon = QtGui.QIcon(food.image)

    # create a delete button
    deleteIcon = QtGui.QIcon(r".\Resources\Images\delete_icon.png")
    btnDelete = QtWidgets.QPushButton()
    btnDelete.setIcon(deleteIcon)
    btnDelete.setIconSize(QtCore.QSize(20, 20))
    deleteSignal = partial(deleteFood, food, ui)

    # add the food to the menu table
    ui.tableMenuFoods.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(food.id)))
    ui.tableMenuFoods.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(foodIcon, "", QtCore.Qt.DecorationRole))
    ui.tableMenuFoods.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(food.title))
    ui.tableMenuFoods.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(str(food.stock)))
    ui.tableMenuFoods.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(food.fixed_price)))
    ui.tableMenuFoods.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(food.sale_price)))

    # add the delete button to the delete column
    ui.tableMenuFoods.setCellWidget(rowCount, 6, btnDelete)

    # connect the delete button to the delete signal
    btnDelete.clicked.connect(deleteSignal)


def deleteFood(food: Food, ui: "Ui_MainWindow"):
    """Delete a food from the menu table"""

    # get the number of rows in the menu table
    rowCount = ui.tableMenuFoods.rowCount()

    # get the row of the food to be deleted
    for i in range(rowCount):
        if food.id == int(ui.tableMenuFoods.item(i, 0).text()):
            row = i
            break

    # delete the food from the menu table
    ui.tableMenuFoods.removeRow(row)

    # update the menu table
    ui.tableMenuFoods.update()


def clearMenuTable(ui: "Ui_MainWindow"):
    """clear menu table"""
    
    # get the number of rows in the menu table
    rowCount = ui.tableMenuFoods.rowCount()

    # delete all rows from the menu table
    for i in range(rowCount):
        ui.tableMenuFoods.removeRow(i)

    # update the menu table
    ui.tableMenuFoods.update()

    # reset the calendarDate
    ui.calendarDate.setSelectedDate(QtCore.QDate.currentDate())


def addMenu(ui: "Ui_MainWindow"):
    """Add a menu"""

    # get the date of the menu
    date = ui.calendarDate.selectedDate()

    # check if the date today or after
    if date < QtCore.QDate.currentDate():
        Messages.push(Messages.Type.ERROR, "Date must be today or after")
        Messages.show()
        return
    
    # create a date object from datetime class of the date
    date = dt.datetime(date.year(), date.month(), date.day()).strftime("%Y-%m-%d")
    
    # check if the date is already in the database
    if Menu.ExistsByDate(date):
        Messages.push(Messages.Type.ERROR, "Menu for this date already exists")
        Messages.show()
        return

    # get the food ids from the menu table
    foodIds = getFoodIds(ui)    

    # fetch foods from the database
    foods: list[Food] = []
    for foodId in foodIds:
        foods.append(Food.Get(foodId))

    # check if the food ids is empty
    if len(foodIds) == 0:
        Messages.push(Messages.Type.ERROR, "Menu must contain at least one food")
        Messages.show()
        return

    foods = [
        {
            "id": food.id,
            "title": food.title,
            "stock": food.stock,
            "fixed_price": food.fixed_price,
            "sale_price": food.sale_price,
            "image": food.image,
            "description": food.description,
            "category": food.category,
            "materials": food.materials,
        } for food in foods
    ]

    # check if the title is not empty
    if ui.lEditMenuTitle.text() == "":
        Messages.push(Messages.Type.ERROR, "Title must not be empty")
        Messages.show()
        return

    data = {
        "title" : ui.lEditMenuTitle.text(),
        "foods" : foods,
        "date" : date,
    }

    # add the menu to the database
    Menu.Create(data)

    # clear the menu table
    clearMenuTable(ui)

    # set up the menu table
    setUpInitInformation(ui)

    # show a message
    Messages.push(Messages.Type.SUCCESS, "Menu added successfully")
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
        
        self.lblMenuTitle = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblMenuTitle.setFont(font)
        self.lblMenuTitle.setObjectName("lblMenuTitle")
        self.gridLayout.addWidget(self.lblMenuTitle, 3, 0, 1, 1)

        self.lEditMenuTitle = QtWidgets.QLineEdit()
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
        
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(lambda:clearMenuTable(self))
        self.btnHLayout.addWidget(self.btnClear)
        
        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(lambda:addMenu(self))
        self.btnHLayout.addWidget(self.btnAdd)
        
        self.gridLayout.addLayout(self.btnHLayout, 5, 0, 1, 2)
        
        self.tableMenuFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        
        self.calendarDate = QtWidgets.QCalendarWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        self.calendarDate.setSizePolicy(sizePolicy)
        self.calendarDate.setObjectName("calendarDate")
        self.gridLayout.addWidget(self.calendarDate, 4, 0, 1, 2)
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(20)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)
        
        self.tableFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.lblMenuTitle.setText(_translate("MainWindow", "Menu Title: "))
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
        self.lblTitle.setText(_translate("MainWindow", "New Menu"))
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

        # check for credentials
        checkForCredentials(MainWindow)

        # setUp intial information
        setUpInitInformation(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
