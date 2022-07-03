from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Food import Food
from Window import Routing
from Window import Transfer
from Controllers.AuthenticationController import Auth
from functools import partial
from Lib.Questions import Questions
from Lib.Messages import Messages


# ////////////////////////////EVENTS////////////////////////////

def setInitInformation(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """Fetches foods from the database and show them in the table."""
    
    # check if the user is admin
    if not Auth.CheckAdminCredentials():
        # logout the user
        Auth.Logout()
        # go to the landing page
        Routing.Redirect(window, 'landingPage')
        Routing.ClearStack() # reset the previous window
        return

    # get all foods from database
    foods = Food.GetAll()

    # set table row count
    ui.tableFoods.setRowCount(len(foods))

    # set table data
    for i, food in enumerate(foods):

        # create a delete button
        deleteIcon = QtGui.QIcon(r".\Resources\Images\delete_icon.png")
        btnDelete = QtWidgets.QPushButton()
        btnDelete.setIcon(deleteIcon)
        btnDelete.setIconSize(QtCore.QSize(20, 20))
        deleteSignal = partial(deleteFood, food.id, window)

        # create a button to go to the food edit window
        editIcon = QtGui.QIcon(r".\Resources\Images\edit_icon.png")
        btnGoToEdit = QtWidgets.QPushButton()
        btnGoToEdit.setIcon(editIcon)
        btnGoToEdit.setIconSize(QtCore.QSize(20, 20))
        editSignal = partial(goToFoodEdit, food.id, window)

        # create a icon of the food image
        foodIcon = QtGui.QIcon(food.image)

        ui.tableFoods.setItem(i, 0, QtWidgets.QTableWidgetItem(str(food.id)))
        ui.tableFoods.setItem(i, 1, QtWidgets.QTableWidgetItem(foodIcon, "", QtCore.Qt.DecorationRole))
        ui.tableFoods.setItem(i, 2, QtWidgets.QTableWidgetItem(food.title))
        ui.tableFoods.setItem(i, 3, QtWidgets.QTableWidgetItem(str(food.stock)))
        ui.tableFoods.setItem(i, 4, QtWidgets.QTableWidgetItem(str(food.fixed_price)))
        ui.tableFoods.setItem(i, 5, QtWidgets.QTableWidgetItem(str(food.sale_price)))
        # add the edit button to edit column
        ui.tableFoods.setCellWidget(i, 6, btnGoToEdit)

        # add the delete button to delete column
        ui.tableFoods.setCellWidget(i, 7, btnDelete)

        # connect edit button to the partial function 
        btnGoToEdit.clicked.connect(editSignal)

        # connect delete button to the partial function
        btnDelete.clicked.connect(deleteSignal)


def goToFoodEdit(id: int, window: 'QtWidgets.QMainWindow'):
    """Go to the food edit window"""

    # save the food object in Transfer
    Transfer.Add("id", id)
    
    # go to the food edit window
    Routing.Redirect(window, 'foodEdit')


def deleteFood(id: int, window: 'QtWidgets.QMainWindow'):
    """Delete a food from the database"""

    # Check if the user is sure
    if not Questions.ask(Questions.Type.ASKOKCANCEL, "Are you sure you want to delete this food?"):
        return

    # delete the food from database
    Food.Delete(id)

    # show success message
    Messages.push(Messages.Type.SUCCESS, "Food deleted successfully")

    # refresh the page
    Routing.Refresh(window)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 850, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 2)
        
        self.tableFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableFoods.setObjectName("tableFoods")
        self.tableFoods.setColumnCount(8)
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

        item = QtWidgets.QTableWidgetItem()
        self.tableFoods.setHorizontalHeaderItem(7, item)

        # set table row height
        self.tableFoods.setRowHeight(0, 30)

        # set table column width
        self.tableFoods.setColumnWidth(0, 10) # id
        self.tableFoods.setColumnWidth(1, 70) # image
        self.tableFoods.setColumnWidth(2, 150) # title
        self.tableFoods.setColumnWidth(3, 150) # stock
        self.tableFoods.setColumnWidth(4, 150) # fixed price
        self.tableFoods.setColumnWidth(5, 150) # sale price
        self.tableFoods.setColumnWidth(6, 50) # edit
        self.tableFoods.setColumnWidth(7, 50) # delete

        # set table edit behavior (not editable)
        self.tableFoods.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.gridLayout.addWidget(self.tableFoods, 1, 0, 1, 2)

        # push button going to the previous window
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnBack.setObjectName("btnBack")
        self.gridLayout.addWidget(self.btnBack, 2, 0, 1, 1)
        self.btnBack.clicked.connect(lambda: Routing.RedirectBack(MainWindow))

        # push button for adding a new food
        self.btnAddFood = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAddFood.setObjectName("btnAddFood")
        self.gridLayout.addWidget(self.btnAddFood, 2, 1, 1, 1)
        self.btnAddFood.clicked.connect(lambda: Routing.Redirect(MainWindow, 'newFood'))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Foods\n"))
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
        item.setText(_translate("MainWindow", "Edit"))
        item = self.tableFoods.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Delete"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnAddFood.setText(_translate("MainWindow", "Add Food"))

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
