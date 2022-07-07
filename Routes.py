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


    def editRestaurant():
        from Views.Admin.EditRestaurantInfoUI import Ui_MainWindow
        return Ui_MainWindow


    def menusPage():
        from Views.Admin.MenusUI import Ui_MainWindow
        return Ui_MainWindow


    def newMenu():
        from Views.Admin.NewMenuUI import Ui_MainWindow
        return Ui_MainWindow


    def editMenu():
        from Views.Admin.EditMenuUI import Ui_MainWindow
        return Ui_MainWindow


    def userInfo():
        from Views.User.InfoUI import Ui_MainWindow
        return Ui_MainWindow

    def cart():
        from Views.User.CartUI import Ui_MainWindow
        return Ui_MainWindow


    def giftCards():
        from Views.Admin.GiftCardsUI import Ui_MainWindow
        return Ui_MainWindow


    def newGiftCard():
        from Views.Admin.NewGiftCardUI import Ui_MainWindow
        return Ui_MainWindow


    def chatRoom():
        from Views.Admin.ChatUI import Ui_MainWindow
        return Ui_MainWindow


    def history():
        from Views.User.OrdersHistoryUI import Ui_MainWindow
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
        "editRestaurant": editRestaurant,
        "userHome" : userInfo,
        "menus" : menusPage,
        "newMenu" : newMenu,
        "menuEdit" : editMenu,
        "userInfo" : userInfo,
        "cart" : cart,
        "giftCards" : giftCards,
        "newGiftCard" : newGiftCard,
        "chatRoom" : chatRoom,
        "history" : history,

    }








