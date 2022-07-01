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



    #UI table window { name : UI method }
    UiObjects = {

        "main" : landingPage,
        "login" : login,
        "signup" : signup,
    }








