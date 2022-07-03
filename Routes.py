class Routes:

    #UI class methods
    #each method returns UI class for a particular window


    def landingPage():
        from Views.LandingPage import Ui_HomeWindow
        return Ui_HomeWindow


    def login():
        from Views.LoginUI import Ui_MainWindow
        return Ui_MainWindow


    def signup():
        from Views.SignUpUI import Ui_MainWindow
        return Ui_MainWindow


    def adminHome():
        from Views.Admin.HomeUI import Ui_MainWindow
        return Ui_MainWindow

    
    def foods():
        from Views.Admin.FoodsUI import Ui_MainWindow
        return Ui_MainWindow


    def editFood():
        from Views.Admin.EditFoodUI import Ui_MainWindow
        return Ui_MainWindow


    def newFood():
        from Views.Admin.NewFoodUI import Ui_MainWindow
        return Ui_MainWindow


    #UI table window { name : UI method }
    UiObjects = {

        "main" : landingPage,
        "login" : login,
        "signup" : signup,
        "adminHome": adminHome,
        "foods" : foods,
        "foodEdit" : editFood,
        "newFood" : newFood,
    }








