from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Food import Food
from Window import Routing
from Window import Transfer


# ////////////////////////////EVENTS////////////////////////////

def setInitInformation(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """Fetches foods from the database and show them in the table."""
    
    # get all foods from database
    foods = Food.GetAll()

    # set table row count
    ui.tableFoods.setRowCount(len(foods))

    # set table data
    for i, food in enumerate(foods):
        
        # create a icon of the food image
        foodIcon = QtGui.QIcon(food.image)

        # create a button to go to the food edit window
        editIcon = QtGui.QIcon(r".\Resources\Images\edit_icon.png")
        btnGoToEdit = QtWidgets.QPushButton()
        btnGoToEdit.setIcon(editIcon)
        btnGoToEdit.setIconSize(QtCore.QSize(20, 20))
        btnGoToEdit.clicked.connect(lambda: goToFoodEdit(food, window))

        ui.tableFoods.setItem(i, 0, QtWidgets.QTableWidgetItem(str(food.id)))
        ui.tableFoods.setItem(i, 1, QtWidgets.QTableWidgetItem(foodIcon, "", QtCore.Qt.DecorationRole))
        ui.tableFoods.setItem(i, 2, QtWidgets.QTableWidgetItem(food.title))
        ui.tableFoods.setItem(i, 3, QtWidgets.QTableWidgetItem(str(food.stock)))
        ui.tableFoods.setItem(i, 4, QtWidgets.QTableWidgetItem(str(food.fixed_price)))
        ui.tableFoods.setItem(i, 5, QtWidgets.QTableWidgetItem(str(food.sale_price)))
        # add the push button to action column
        ui.tableFoods.setCellWidget(i, 6, btnGoToEdit)

    # set table row height
    ui.tableFoods.setRowHeight(0, 30)

    # set table column width
    ui.tableFoods.setColumnWidth(0, 10) # id
    ui.tableFoods.setColumnWidth(1, 70) # image
    ui.tableFoods.setColumnWidth(2, 150) # title
    ui.tableFoods.setColumnWidth(3, 150) # stock
    ui.tableFoods.setColumnWidth(4, 150) # fixed price
    ui.tableFoods.setColumnWidth(5, 150) # sale price
    ui.tableFoods.setColumnWidth(6, 100) # action

    # set table edit behavior (not editable)
    ui.tableFoods.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


def goToFoodEdit(food:Food, window: 'QtWidgets.QMainWindow'):
    """Go to the food edit window"""

    # save the food object in Transfer
    Transfer.Add("food", food)
    
    # go to the food edit window
    Routing.Redirect(window, 'foodEdit')


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
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)
        
        self.tableFoods = QtWidgets.QTableWidget(self.gridLayoutWidget)
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

        self.gridLayout.addWidget(self.tableFoods, 1, 0, 1, 1)
        
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
        item.setText(_translate("MainWindow", "Action"))

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
