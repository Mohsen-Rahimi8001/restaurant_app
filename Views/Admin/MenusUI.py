from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Controllers.Admin.MenusController import MenusController
from Window import Routing, Transfer
from Models.Menu import Menu
from functools import partial
from Lib.Messages import Messages
from Lib.Questions import Questions



def checkForCredentials(window: "QtWidgets.QMainWindow"):
    """check if the user is logged in and is an admin"""
    
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


def setUpInitInformation(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """Fetches menus from the database and show them in the table."""

    # get default menus
    defaultMenus = MenusController.GetDefaultMenus()

    # get all menus from database
    menus = Menu.GetAll()
    
    # set default menus table row count
    ui.tableDefaultMenus.setRowCount(len(defaultMenus))
    
    # set table row count
    ui.tableMenus.setRowCount(len(menus))


    # add defualt menus
    for i, menu in enumerate(defaultMenus):
        
        # create edit button
        editButton = QtWidgets.QPushButton()
        editButton.setIcon(QtGui.QIcon(r'.\Resources\Images\edit_icon.png'))
        editButton.setIconSize(QtCore.QSize(20, 20))
        editSignal = partial(goToMenuEdit, i+1)

        # set menu id
        ui.tableDefaultMenus.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))

        # set menu title
        ui.tableDefaultMenus.setItem(i, 1, QtWidgets.QTableWidgetItem(menu.title))

        # set menu foods
        foods = ""
        for food in menu.foods:
            foods += food['title'] + ", "
    
        ui.tableDefaultMenus.setItem(i, 2, QtWidgets.QTableWidgetItem(foods))

        # set menu weekday
        ui.tableDefaultMenus.setItem(i, 3, QtWidgets.QTableWidgetItem(menu.date))

        # set menu edit button
        ui.tableDefaultMenus.setCellWidget(i, 4, editButton)

        # connect edit button to goToMenuEdit function
        editButton.clicked.connect(editSignal)


    # set table data
    for i, menu in enumerate(menus):

        # create a delete button
        deleteIcon = QtGui.QIcon(r".\Resources\Images\delete_icon.png")
        btnDelete = QtWidgets.QPushButton()
        btnDelete.setIcon(deleteIcon)
        btnDelete.setIconSize(QtCore.QSize(20, 20))
        deleteSignal = partial(deleteMenu, menu.id, window)

        # create a button to go to the menu edit window
        editIcon = QtGui.QIcon(r".\Resources\Images\edit_icon.png")
        btnGoToEdit = QtWidgets.QPushButton()
        btnGoToEdit.setIcon(editIcon)
        btnGoToEdit.setIconSize(QtCore.QSize(20, 20))
        editSignal = partial(goToMenuEdit, menu.id, window)

        ui.tableMenus.setItem(i, 0, QtWidgets.QTableWidgetItem(str(menu.id)))
        ui.tableMenus.setItem(i, 1, QtWidgets.QTableWidgetItem(menu.title))
        
        foods = ""
        for food in menu.foods:
            foods += food['title'] + ", "

        ui.tableMenus.setItem(i, 2, QtWidgets.QTableWidgetItem(foods))

        ui.tableMenus.setItem(i, 3, QtWidgets.QTableWidgetItem(menu.date))
        
        # set delete button
        ui.tableMenus.setCellWidget(i, 4, btnDelete)

        # connect edit button to goToMenuEdit function
        btnGoToEdit.clicked.connect(editSignal)

        # set edit button
        ui.tableMenus.setCellWidget(i, 5, btnGoToEdit)

        # connect delete button to deleteMenu function
        btnDelete.clicked.connect(deleteSignal)


# ////////////////////////////////EVENTS////////////////////////////
def goToMenuEdit(id: int, window: 'QtWidgets.QMainWindow'):
    """go to the menu edit window"""

    # store the menu id to transfer to the next window
    Transfer.Add('id', id)

    # go to the menu edit window
    Routing.Redirect(window, 'menuEdit')


def deleteMenu(id: int, window: 'QtWidgets.QMainWindow'):
    """delete a menu"""

    # check if the admin is sure about deleting the menu
    if Questions.ask(Questions.Type.ASKYESNO, "Are you sure you want to delete this menu?"):
        # delete the menu
        Menu.Delete(id)

        # show a message
        Messages.push(Messages.Type.SUCCESS, "Menu deleted successfully.")
        
        # refresh the table
        Routing.Refresh(window)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 710)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 720, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        
        self.tableMenus = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.tableMenus.sizePolicy().hasHeightForWidth())
        self.tableMenus.setSizePolicy(sizePolicy)
        self.tableMenus.setObjectName("tableMenus")
        self.tableMenus.setColumnCount(6)
        self.tableMenus.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(0, item) # id
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(1, item) # title
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(2, item) # foods
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(3, item) # date
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(4, item) # edit button
        
        item = QtWidgets.QTableWidgetItem()
        self.tableMenus.setHorizontalHeaderItem(5, item) # delete button
        
        # set table column width
        self.tableMenus.setColumnWidth(0, 10) # id
        self.tableMenus.setColumnWidth(1, 70) # title
        self.tableMenus.setColumnWidth(2, 300) # foods
        self.tableMenus.setColumnWidth(3, 100) # date
        self.tableMenus.setColumnWidth(4, 70) # edit button
        self.tableMenus.setColumnWidth(5, 70) # delete button

        # set table edit behavior (not editable)
        self.tableMenus.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.gridLayout.addWidget(self.tableMenus, 2, 0, 1, 1)
        
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda: Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        
        self.btnAddMenu = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnAddMenu.setFont(font)
        self.btnAddMenu.setObjectName("btnAddMenu")
        self.btnAddMenu.clicked.connect(lambda:Routing.Redirect(MainWindow, 'newMenu'))
        self.btnHLayout.addWidget(self.btnAddMenu)
        self.gridLayout.addLayout(self.btnHLayout, 3, 0, 1, 1)
        
        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)

        self.tableDefaultMenus = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.tableDefaultMenus.sizePolicy().hasHeightForWidth())
        self.tableDefaultMenus.setSizePolicy(sizePolicy)
        self.tableDefaultMenus.setObjectName("tableDefaultMenus")
        self.tableDefaultMenus.setColumnCount(5)
        self.tableDefaultMenus.setRowCount(0)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableDefaultMenus.setHorizontalHeaderItem(0, item) # id
        
        item = QtWidgets.QTableWidgetItem()
        self.tableDefaultMenus.setHorizontalHeaderItem(1, item) # title
        
        item = QtWidgets.QTableWidgetItem()
        self.tableDefaultMenus.setHorizontalHeaderItem(2, item) # foods
        
        item = QtWidgets.QTableWidgetItem()
        self.tableDefaultMenus.setHorizontalHeaderItem(3, item) # date
        
        item = QtWidgets.QTableWidgetItem()
        self.tableDefaultMenus.setHorizontalHeaderItem(4, item) # edit button
        
        # set table column width
        self.tableDefaultMenus.setColumnWidth(0, 10) # id
        self.tableDefaultMenus.setColumnWidth(1, 100) # title
        self.tableDefaultMenus.setColumnWidth(2, 340) # foods
        self.tableDefaultMenus.setColumnWidth(3, 100) # date
        self.tableDefaultMenus.setColumnWidth(4, 70) # edit button

        # set table edit behavior (not editable)
        self.tableDefaultMenus.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


        self.gridLayout.addWidget(self.tableDefaultMenus, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableMenus.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableMenus.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableMenus.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Foods"))
        item = self.tableMenus.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableMenus.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Edit"))
        item = self.tableMenus.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delete"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnAddMenu.setText(_translate("MainWindow", "Add Menu"))
        self.lblTitle.setText(_translate("MainWindow", "Menus"))
        item = self.tableDefaultMenus.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableDefaultMenus.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableDefaultMenus.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Foods"))
        item = self.tableDefaultMenus.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableDefaultMenus.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Edit"))

        # check for credentials
        checkForCredentials(MainWindow)

        # set up intial information
        setUpInitInformation(self, MainWindow)

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
