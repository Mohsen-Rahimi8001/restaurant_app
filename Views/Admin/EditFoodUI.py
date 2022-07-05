from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Food import Food
from Window import Routing, Transfer
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Lib.Questions import Questions
import os


FOOD: Food = None


def setFoodObject():
    """This function sets the food object to the global variable FOOD"""
    global FOOD
    
    foodId = Transfer.Get('id')
    FOOD = Food.Get(foodId)


# /////////////////////////////EVENTS////////////////////////////
def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """checks if the user is admin"""

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


def setupInitInformation(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """sets the information of the selected food to be edited"""

    # check if the FOOD is not None
    if not FOOD:
        Messages.push(Messages.Type.ERROR, "Something wrong with initialization.")
        Messages.show()
        # redirect back
        Routing.RedirectBack(window)
        return

    # set the food image to lblFoodPicture as a QPixmap
    ui.lblFoodPicture.setPixmap(QtGui.QPixmap(FOOD.image))
    ui.lblFoodPicture.setScaledContents(True)

    # set the food title
    ui.lEditNewTitle.setText(FOOD.title)

    # set the food stock
    ui.lEditNewStock.setText(str(FOOD.stock))

    # set the food fixed price
    ui.lEditNewFixedPrice.setText(str(FOOD.fixed_price))

    # set the food sale price
    ui.lEditNewSalePrice.setText(str(FOOD.sale_price))

    # set the food description
    ui.lEditNewDescription.setText(FOOD.description)

    # set the food category
    ui.lEditNewCategory.setText(FOOD.category)

    # set the food materials
    ui.lEditNewMaterial.setText(FOOD.materials)

    # set the food image
    ui.lEditNewImage.setText(FOOD.image)


def clearPage(ui: "Ui_MainWindow"):
    """clears the page"""

    # clear the food image
    ui.lblFoodPicture.clear()

    # clear the food title
    ui.lEditNewTitle.clear()

    # clear the food stock
    ui.lEditNewStock.clear()

    # clear the food fixed price
    ui.lEditNewFixedPrice.clear()

    # clear the food sale price
    ui.lEditNewSalePrice.clear()

    # clear the food description
    ui.lEditNewDescription.clear()

    # clear the food category
    ui.lEditNewCategory.clear()

    # clear the food materials
    ui.lEditNewMaterial.clear()

    # clear the food image
    ui.lEditNewImage.clear()


def browseForImage(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """browses for an image"""

    # open a file dialog
    fileName = QtWidgets.QFileDialog.getOpenFileName(window, "Open File", ".", "Image Files (*.png *.jpg *.bmp *.gif)")

    # if the user didn't select an image
    if fileName[0] == "":
        return

    # set the image to the lblFoodPicture
    ui.lblFoodPicture.setPixmap(QtGui.QPixmap(fileName[0]))
    ui.lblFoodPicture.setScaledContents(True)

    # set the image path to the lEditNewImage
    ui.lEditNewImage.setText(fileName[0])


def saveChanges(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """change the food information in the database"""
    
    # new data for the food
    newData = dict()

    # get the new information from the UI
    title = ui.lEditNewTitle.text()
    
    if title: 
        newData['title'] = title

    try:
        newData['stock'] = int(ui.lEditNewStock.text())
    except ValueError:
        # Show Error Massege
        Messages.push(Messages.Type.ERROR, "Stock must be an integer")
        Messages.show()
        return

    try:
        newData['fixed_price'] = int(ui.lEditNewFixedPrice.text())
    except ValueError:
        # Show Error Massege
        Messages.push(Messages.Type.ERROR, "Fixed Price must be an integer")
        Messages.show()
        return
    
    try:
        newData['sale_price'] = int(ui.lEditNewSalePrice.text())
    except ValueError:
        # Show Error Massege
        Messages.push(Messages.Type.ERROR, "Sale Price must be an integer")
        Messages.show()
        return
    

    if description := ui.lEditNewDescription.text():
        newData['description'] = description

    if category := ui.lEditNewCategory.text():
        newData['category'] = category

    if materials := ui.lEditNewMaterial.text():
        newData['materials'] = materials

    if image := ui.lEditNewImage.text():
        newData['image'] = image

    # check if it is a valid image directory
    if not os.path.isfile(image):
        # Show Warning Massege
        if not Questions.ask(Questions.Type.ASKYESNO, "The image directorys doesn't exist.\n"
            "Do you want to set the default image to the food?"):
            return

    # update the food information in the database
    try:
        Food.Update(FOOD.id, newData)
    except Exception as e:
        # Show Error Massege
        Messages.push(Messages.Type.ERROR, str(e))
        Messages.show()
    else:
        # show success message
        Messages.push(Messages.Type.SUCCESS, "the food was updated successfully")
        Messages.show()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 771, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.lblNewSalePrice = QtWidgets.QLabel(self.gridLayoutWidget)

        self.lblFoodPicture = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        self.lblFoodPicture.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.lblFoodPicture.setFont(font)
        self.lblFoodPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFoodPicture.setObjectName("lblFoodPicture")
        self.gridLayout.addWidget(self.lblFoodPicture, 0, 0, 1, 3)

        self.lblNewTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewTitle.setFont(font)
        self.lblNewTitle.setObjectName("lblNewTitle")
        self.gridLayout.addWidget(self.lblNewTitle, 1, 0, 1, 1)

        self.lEditNewTitle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewTitle.setInputMask("")
        self.lEditNewTitle.setText("")
        self.lEditNewTitle.setClearButtonEnabled(True)
        self.lEditNewTitle.setObjectName("lEditNewTitle")
        self.gridLayout.addWidget(self.lEditNewTitle, 1, 1, 1, 2)

        self.lblNewStock = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewStock.setFont(font)
        self.lblNewStock.setObjectName("lblNewStock")
        self.gridLayout.addWidget(self.lblNewStock, 2, 0, 1, 1)

        self.lEditNewStock = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewStock.setClearButtonEnabled(True)
        self.lEditNewStock.setObjectName("lEditNewStock")
        self.gridLayout.addWidget(self.lEditNewStock, 2, 1, 1, 2)

        self.lblNewFixedPrice = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewFixedPrice.setFont(font)
        self.lblNewFixedPrice.setObjectName("lblNewFixedPrice")
        self.gridLayout.addWidget(self.lblNewFixedPrice, 3, 0, 1, 1)

        self.lEditNewFixedPrice = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewFixedPrice.setClearButtonEnabled(True)
        self.lEditNewFixedPrice.setObjectName("lEditNewFixedPrice")
        self.gridLayout.addWidget(self.lEditNewFixedPrice, 3, 1, 1, 2)

        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewSalePrice.setFont(font)
        self.lblNewSalePrice.setObjectName("lblNewSalePrice")
        self.gridLayout.addWidget(self.lblNewSalePrice, 4, 0, 1, 1)

        self.lEditNewSalePrice = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewSalePrice.setClearButtonEnabled(True)
        self.lEditNewSalePrice.setObjectName("lEditNewSalePrice")
        self.gridLayout.addWidget(self.lEditNewSalePrice, 4, 1, 1, 2)

        self.lblNewDescription = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewDescription.setFont(font)
        self.lblNewDescription.setObjectName("lblNewDescription")
        self.gridLayout.addWidget(self.lblNewDescription, 5, 0, 1, 1)

        self.lEditNewDescription = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewDescription.setClearButtonEnabled(True)
        self.lEditNewDescription.setObjectName("lEditNewDescription")
        self.gridLayout.addWidget(self.lEditNewDescription, 5, 1, 1, 2)

        self.lblNewCategory = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewCategory.setFont(font)
        self.lblNewCategory.setObjectName("lblNewCategory")
        self.gridLayout.addWidget(self.lblNewCategory, 6, 0, 1, 1)

        self.lEditNewCategory = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewCategory.setClearButtonEnabled(True)
        self.lEditNewCategory.setObjectName("lEditNewCategory")
        self.gridLayout.addWidget(self.lEditNewCategory, 6, 1, 1, 2)

        self.lblNewMaterial = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewMaterial.setFont(font)
        self.lblNewMaterial.setObjectName("lblNewMaterial")
        self.gridLayout.addWidget(self.lblNewMaterial, 7, 0, 1, 1)

        self.lEditNewMaterial = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewMaterial.setClearButtonEnabled(True)
        self.lEditNewMaterial.setObjectName("lEditNewMaterial")
        self.gridLayout.addWidget(self.lEditNewMaterial, 7, 1, 1, 2)

        self.lblNewImage = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblNewImage.setFont(font)
        self.lblNewImage.setObjectName("lblNewImage")
        self.gridLayout.addWidget(self.lblNewImage, 8, 0, 1, 1)

        self.lEditNewImage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditNewImage.setClearButtonEnabled(True)
        self.lEditNewImage.setObjectName("lEditNewImage")
        self.gridLayout.addWidget(self.lEditNewImage, 8, 1, 1, 1)

        self.btnBrowseImageFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBrowseImageFile.setFont(font)
        self.btnBrowseImageFile.setObjectName("btnBrowseImageFile")
        self.btnBrowseImageFile.clicked.connect(lambda: browseForImage(self, MainWindow))
        self.gridLayout.addWidget(self.btnBrowseImageFile, 8, 2, 1, 1)

        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setContentsMargins(-1, 20, -1, -1)
        self.btnHLayout.setSpacing(20)
        self.btnHLayout.setObjectName("btnHLayout")
        self.btnBack = QtWidgets.QPushButton(self.gridLayoutWidget)
        
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(lambda : Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(lambda : clearPage(self))
        self.btnHLayout.addWidget(self.btnClear)

        self.btnRefresh = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.clicked.connect(lambda : setupInitInformation(self, MainWindow))
        self.btnHLayout.addWidget(self.btnRefresh)
        
        self.btnChange = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnChange.setFont(font)
        self.btnChange.setObjectName("btnChange")
        self.btnHLayout.addWidget(self.btnChange)
        self.btnChange.clicked.connect(lambda : saveChanges(self, MainWindow))
        self.gridLayout.addLayout(self.btnHLayout, 9, 0, 1, 3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: 'QtWidgets.QMainWindow'):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblNewSalePrice.setText(_translate("MainWindow", "New Sale Price: "))
        self.lEditNewMaterial.setPlaceholderText(_translate("MainWindow", "New Material"))
        self.lblNewImage.setText(_translate("MainWindow", "New Image: "))
        self.lblNewTitle.setText(_translate("MainWindow", "New Title: "))
        self.lblNewStock.setText(_translate("MainWindow", "New Stock: "))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnRefresh.setText(_translate("MainWindow", "Retrieve Information"))
        self.btnChange.setText(_translate("MainWindow", "Change"))
        self.lEditNewCategory.setPlaceholderText(_translate("MainWindow", "New Category"))
        self.lEditNewImage.setPlaceholderText(_translate("MainWindow", "New Image Directory"))
        self.lEditNewFixedPrice.setPlaceholderText(_translate("MainWindow", "New Fixed Price"))
        self.lblNewMaterial.setText(_translate("MainWindow", "New Material: "))
        self.lblNewCategory.setText(_translate("MainWindow", "New Category: "))
        self.lblNewDescription.setText(_translate("MainWindow", "New Description: "))
        self.lblNewFixedPrice.setText(_translate("MainWindow", "New Fixed Price: "))
        self.lEditNewStock.setPlaceholderText(_translate("MainWindow", "New Stock"))
        self.lblFoodPicture.setText(_translate("MainWindow", "Food"))
        self.btnBrowseImageFile.setText(_translate("MainWindow", "Browse"))
        self.lEditNewTitle.setPlaceholderText(_translate("MainWindow", "New Title"))
        self.lEditNewDescription.setPlaceholderText(_translate("MainWindow", "New Description"))
        self.lEditNewSalePrice.setPlaceholderText(_translate("MainWindow", "New Sale Price"))

        setFoodObject()
        checkForCredentials(MainWindow)
        setupInitInformation(self, MainWindow)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
