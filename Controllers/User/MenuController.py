from Controllers.Validation import DateValidator
from Models.Menu import Menu
from Lib.DateTools import DateTools
from Lib.Messages import Messages
from Controllers.User.CartController import Cart


class MenuController:


    @staticmethod
    def ValidateDateInput(year : str, month : str, day : str) -> bool:

        valid = DateValidator.ValidateDay(day)
        valid &= DateValidator.ValidateMonth(month)
        valid &= DateValidator.ValidateYear(year)
        return valid


    @staticmethod
    def SearchDate(year : str, month : str, day : str) -> "list[Menu]":

        if not MenuController.ValidateDateInput(year, month, day):
            return False

        date = DateTools.GetDateStrFormat(year, month, day)

        if not Menu.ExistsByDate(date):
            Messages.push(Messages.Type.INFO, "there is no menu for specified date")
            return False

        menus = Menu.GetByDate(date)

        return menus


    @staticmethod
    def GetPresentMenus():
        """returns menus that their date is not past"""

        menus : "list[Menu]" = Menu.GetAll()

        result = []

        for menu in menus:

            if DateTools.Compare( DateTools.GetToday(), menu.date ) != -1:
                result.append(menu)


        return result


