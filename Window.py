from PyQt5.QtWidgets import *
from Lib.Messages import Messages



class Routing:

    CurrentWindow = "adminHome"
    PreviousWindow = []


    @classmethod
    def ClearStack(cls):
        """Flush the routing stack"""
        cls.PreviousWindow.clear()


    @staticmethod
    def Redirect(currentWindowObject, nextWindowName : str) -> None:
        """switch window to nextWindowName"""

        Routing.PreviousWindow.append(Routing.CurrentWindow)
        Routing.CurrentWindow = nextWindowName

        #create new window
        currentWindowObject.cams = Window()

        #delete current window
        currentWindowObject.close()


    @staticmethod
    def RedirectBack(currentWindowObject):
        """back to previous window"""

        if Routing.PreviousWindow:
            Routing.CurrentWindow = Routing.PreviousWindow.pop()
        
            # create new window
            currentWindowObject.cams = Window()

            # delete current window
            currentWindowObject.close()
            


    @staticmethod
    def Refresh(currentWindowObject):
        """refresh window"""

        # create new window
        currentWindowObject.cams = Window()

        # delete current window
        currentWindowObject.close()




class Transfer:

    #store data to transfer it to another window
    Data = {}

    @staticmethod
    def Add(name : str, data) -> None:
        """add data to transfer to another window"""
        Transfer.Data.update({ name : data })


    @staticmethod
    def Exists(name : str) -> bool:
        """check if a data is in transfer or not"""
        return name in Transfer.Data.keys()


    @staticmethod
    def Get(name : str):
        """get transferred data"""

        if Transfer.Exists(name):

            data = Transfer.Data[name]
            Transfer.Data.pop(name)
            return data

        else:
            return False




class Window(QMainWindow):
    """ app main window class """

    def __init__(self):

        super().__init__()

        #get current window UI class
        from Routes import Routes
        uiClass =  Routes.UiObjects[ Routing.CurrentWindow ]()

        #instantiate UI class and apply UI to window
        uiClass().setupUi(self)

        # show messages
        Messages.show()

        #show window
        self.show()




