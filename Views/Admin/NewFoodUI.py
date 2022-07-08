from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.AuthenticationController import Auth
from Lib.Messages import Messages
from Lib.Questions import Questions
from Models.Food import Food
from Window import Routing


# ////////////////////////////EVENTS////////////////////////////
def checkForCredentials(window: 'QtWidgets.QMainWindow'):
    """Checks if the user is logged in and has the admin credentials."""
    if not Auth.IsUserLoggedIN() or not Auth.CheckAdminCredentials():
        Routing.Redirect(window, 'main')
        Routing.ClearStack()


def clearPage(ui: "Ui_MainWindow"):
    """Clear the page"""
    ui.lEditTitle.setText("")
    ui.lEditStock.setText("")
    ui.lEditFixedPrice.setText("")
    ui.lEditSalePrice.setText("")
    ui.lEditDescription.setText("")
    ui.lEditCategory.setText("")
    ui.lEditMaterial.setText("")
    ui.lEditImage.setText("")
    ui.lblFoodPicture.setPixmap(QtGui.QPixmap(r".\Resources\Images\food_default.png"))


def browseForImage(ui: "Ui_MainWindow", window: "QtWidgets.QMainWindow"):
    """browses for an image"""

    # open a file dialog
    fileName = QtWidgets.QFileDialog.getOpenFileName(window, "Open File", ".\\", "Image Files (*.png *.jpg *.bmp *.gif)")

    # if the user didn't select an image
    if fileName[0] == "":
        return

    # set the image to the lblFoodPicture
    ui.lblFoodPicture.setPixmap(QtGui.QPixmap(fileName[0]))
    ui.lblFoodPicture.setScaledContents(True)

    # set the image path to the lEditImage
    ui.lEditImage.setText(fileName[0])



def addNewFood(ui: "Ui_MainWindow", window: 'QtWidgets.QMainWindow'):
    """Add a new food to the database"""

    # get the food information from the form
    title = ui.lEditTitle.text()
    stock = ui.lEditStock.text()
    fixed_price = ui.lEditFixedPrice.text()
    sale_price = ui.lEditSalePrice.text()
    description = ui.lEditDescription.text()
    category = ui.lEditCategory.text()
    material = ui.lEditMaterial.text()
    image = ui.lEditImage.text()

    # check if the user entered the necessary information
    # check for title
    if title == "":
        Messages.push(Messages.Type.ERROR, "Please enter a title")
        Messages.show()
        return

    # check for numeric values
    if not stock.isdigit() or not fixed_price.isdigit() or not sale_price.isdigit():
        Messages.push(Messages.Type.ERROR, "Please enter valid numbers in stock, fixed price and sale price")
        Messages.show()
        return
    
    # ask for optional information
    if not description or not category or not material or not image:
        if not Questions.ask(Questions.Type.ASKOKCANCEL, "You didn't enter all the information,\
            \nare you sure you want to add this food?"):
            return

    try:
        # create a new food
        Food.Create({
            "title" : title,
            "stock" : int(stock),
            "fixed_price" : int(fixed_price),
            "sale_price" : int(sale_price),
            "description" : description,
            "category" : category,
            "materials" : material,
            "image" : image,
        })

    except Exception as e:
        # show the error message
        Messages.push(Messages.Type.ERROR, str(e))
        Messages.show()
    else:
        # clear the page
        clearPage(ui)

        # show the user a message
        Messages.push(Messages.Type.SUCCESS, "Food added successfully")
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

        self.lblTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 1, 0, 1, 1)

        self.lEditTitle = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditTitle.setInputMask("")
        self.lEditTitle.setText("")
        self.lEditTitle.setClearButtonEnabled(True)
        self.lEditTitle.setObjectName("lEditTitle")
        self.gridLayout.addWidget(self.lEditTitle, 1, 1, 1, 2)

        self.lblStock = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblStock.setFont(font)
        self.lblStock.setObjectName("lblStock")
        self.gridLayout.addWidget(self.lblStock, 2, 0, 1, 1)

        self.lEditStock = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditStock.setClearButtonEnabled(True)
        self.lEditStock.setObjectName("lEditStock")
        self.gridLayout.addWidget(self.lEditStock, 2, 1, 1, 2)

        self.lblFixedPrice = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblFixedPrice.setFont(font)
        self.lblFixedPrice.setObjectName("lblFixedPrice")
        self.gridLayout.addWidget(self.lblFixedPrice, 3, 0, 1, 1)

        self.lEditFixedPrice = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditFixedPrice.setClearButtonEnabled(True)
        self.lEditFixedPrice.setObjectName("lEditFixedPrice")
        self.gridLayout.addWidget(self.lEditFixedPrice, 3, 1, 1, 2)

        self.lblSalePrice = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblSalePrice.setFont(font)
        self.lblSalePrice.setObjectName("lblSalePrice")
        self.gridLayout.addWidget(self.lblSalePrice, 4, 0, 1, 1)

        self.lEditSalePrice = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditSalePrice.setClearButtonEnabled(True)
        self.lEditSalePrice.setObjectName("lEditSalePrice")
        self.gridLayout.addWidget(self.lEditSalePrice, 4, 1, 1, 2)

        self.lblDescription = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblDescription.setFont(font)
        self.lblDescription.setObjectName("lblDescription")
        self.gridLayout.addWidget(self.lblDescription, 5, 0, 1, 1)

        self.lEditDescription = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditDescription.setClearButtonEnabled(True)
        self.lEditDescription.setObjectName("lEditDescription")
        self.gridLayout.addWidget(self.lEditDescription, 5, 1, 1, 2)

        self.lblCategory = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblCategory.setFont(font)
        self.lblCategory.setObjectName("lblCategory")
        self.gridLayout.addWidget(self.lblCategory, 6, 0, 1, 1)

        self.lEditCategory = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditCategory.setClearButtonEnabled(True)
        self.lEditCategory.setObjectName("lEditCategory")
        self.gridLayout.addWidget(self.lEditCategory, 6, 1, 1, 2)

        self.lblMaterial = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblMaterial.setFont(font)
        self.lblMaterial.setObjectName("lblMaterial")
        self.gridLayout.addWidget(self.lblMaterial, 7, 0, 1, 1)
        
        self.lEditMaterial = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditMaterial.setClearButtonEnabled(True)
        self.lEditMaterial.setObjectName("lEditMaterial")
        self.gridLayout.addWidget(self.lEditMaterial, 7, 1, 1, 2)
        
        self.lblImage = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.lblImage.setFont(font)
        self.lblImage.setObjectName("lblImage")
        self.gridLayout.addWidget(self.lblImage, 8, 0, 1, 1)
        
        self.lEditImage = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lEditImage.setClearButtonEnabled(True)
        self.lEditImage.setObjectName("lEditImage")
        self.gridLayout.addWidget(self.lEditImage, 8, 1, 1, 1)

        self.btnBrowseImageFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnBrowseImageFile.setFont(font)
        self.btnBrowseImageFile.setObjectName("btnBrowseImageFile")
        self.btnBrowseImageFile.clicked.connect(lambda:browseForImage(self, MainWindow))
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
        self.btnBack.clicked.connect(lambda:Routing.RedirectBack(MainWindow))
        self.btnHLayout.addWidget(self.btnBack)
        
        self.btnClear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.clicked.connect(lambda: clearPage(self))
        self.btnHLayout.addWidget(self.btnClear)
        
        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(lambda: addNewFood(self, MainWindow))
        self.btnHLayout.addWidget(self.btnAdd)
        
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
        self.lblSalePrice.setText(_translate("MainWindow", "Sale Price: "))
        self.lEditMaterial.setPlaceholderText(_translate("MainWindow", "The material used in the food"))
        self.lblImage.setText(_translate("MainWindow", "Image: "))
        self.lblTitle.setText(_translate("MainWindow", "Title: "))
        self.lblStock.setText(_translate("MainWindow", "Stock: "))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.lEditCategory.setPlaceholderText(_translate("MainWindow", "Category of the food"))
        self.lEditImage.setPlaceholderText(_translate("MainWindow", "Image Directory"))
        self.lEditFixedPrice.setPlaceholderText(_translate("MainWindow", "Fixed Price"))
        self.lblMaterial.setText(_translate("MainWindow", "Material: "))
        self.lblCategory.setText(_translate("MainWindow", "Category: "))
        self.lblDescription.setText(_translate("MainWindow", "Description: "))
        self.lblFixedPrice.setText(_translate("MainWindow", "Fixed Price: "))
        self.lEditStock.setPlaceholderText(_translate("MainWindow", "The available number of this food"))
        self.lblFoodPicture.setText(_translate("MainWindow", "Food"))
        self.btnBrowseImageFile.setText(_translate("MainWindow", "Browse"))
        self.lEditTitle.setPlaceholderText(_translate("MainWindow", "Title of the new food"))
        self.lEditDescription.setPlaceholderText(_translate("MainWindow", "Description"))
        self.lEditSalePrice.setPlaceholderText(_translate("MainWindow", "Sale Price"))

        # Clear the page
        clearPage(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
