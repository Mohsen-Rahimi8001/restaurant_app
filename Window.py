from PyQt5.QtWidgets import *




class Routing:

    CurrentWindow = "main"
    PreviousWindow = False


    @staticmethod
    def Redirect(currentWindowObject, nextWindowName : str) -> None:
        """switch window to nextWindowName"""

        Routing.PreviousWindow = Routing.CurrentWindow
        Routing.CurrentWindow = nextWindowName

        #create new window
        currentWindowObject.cams = Window()

        #delete current window
        currentWindowObject.close()


    @staticmethod
    def RedirectBack(currentWindowObject):
        """back to previous window"""

        if Routing.PreviousWindow:
            Routing.Redirect(currentWindowObject, Routing.PreviousWindow)







class Window(QMainWindow):
    """ app main window class """

    def __init__(self):
        super().__init__()

        #get current window UI class
        from Routes import Routes
        uiClass =  Routes.UiObjects[ Routing.CurrentWindow ]()

        #instantiate UI class and apply UI to window
        uiClass().setupUi(self)

        #show window
        self.show()



