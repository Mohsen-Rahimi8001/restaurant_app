from Models.Model import Model
import json
from Models.Food import Food
from DataBase.Sqlite import Database
import datetime as dt


class Menu(Model):

    TableName = "menus"
    PrimaryKey = "id"
    DatePattern = "%Y-%m-%d"

    def __init__(self, id : int, title : str, foods : list, date : str):

        super(Menu, self).__init__(id)
        self.title : str = title
        self.foods : list = foods
        self.date : str = date



    @staticmethod
    def ValidateDate(date:str):
        """Validates the date of the Menu
        :param date: The date of the Menu
        :return: date if it is valid, raises proper error otherwise
        """
        try:
            dt.datetime.strptime(date, Menu.DatePattern)
        except ValueError:
            raise ValueError("Incorrect data format, should be 'Year-Month-Day'")

        return date



    @staticmethod
    def Create(menuData : dict):
        """create new menu in database"""

        data = menuData.copy()

        data["date"] = Menu.ValidateDate(data["date"])

        data["foods"] = json.dumps(data["foods"])

        return Database.Create(Menu.TableName, data)



    @staticmethod
    def Get(id : int):
        """returns an Menu Model object representing a row in menus table with"""

        if not Menu.Exists(id):
            raise RuntimeError("menu does not exist")

        row : list = Database.Read(Menu.TableName, Menu.PrimaryKey, id)[0]

        return Menu(
            id = row[0],
            title = row[1],
            foods = json.loads(row[2]) if row[2] else list(),
            date = row[3]
        )


    @staticmethod
    def GetAll() -> list['Menu']:
        """get all orders"""

        rows = Database.ReadAll(Menu.TableName)

        menus = list()

        for row in rows:
            menus.append(Menu(
                id=row[0],
                title=row[1],
                foods=json.loads(row[2]) if row[2] else list(),
                date=row[3]
            ))

        return menus


    @staticmethod
    def Exists(id : int):
        """check if a menu exists in database or not"""

        return Database.Exists(Menu.TableName, Menu.PrimaryKey, id)


    @staticmethod
    def ExistsByDate(date : str):
        """check if a menu exists in database or not"""

        date = Menu.ValidateDate(date)

        return Database.Exists(Menu.TableName, "date", date)


    @staticmethod
    def GetByDate(date : str):
        """returns menus with given date"""

        if not Menu.ExistsByDate(date):
             return False

        rows = Database.Read(Menu.TableName, "date", date)

        menus = list()

        for row in rows:
            menus.append(Menu(
                id=row[0],
                title=row[1],
                foods=json.loads(row[2]) if row[2] else list(),
                date=row[3]
            ))

        return menus


    @staticmethod
    def Update(id : int, menuData):
        """update menu"""

        if not Menu.Exists(id):
            raise RuntimeError("menu does not exist")

        data = menuData.copy()

        if "id" in data.keys():
            data.pop("id")

        if "foods" in data.keys():
            data["foods"] = json.dumps(data["foods"])

        if 'date' in data.keys():
            data['date'] = Menu.ValidateDate(data['date'])

        Database.Update(Menu.TableName, Menu.PrimaryKey, id, data)


    @staticmethod
    def Delete(id : int):
        """delete menu"""

        if not Menu.Exists(id):
            raise RuntimeError("menu does not exist")

        Database.Delete(Menu.TableName, Menu.PrimaryKey, id)


    @staticmethod
    def DeleteAll():
        """Flush all the menus"""
        Database.DeleteAll(Menu.TableName)


    @staticmethod
    def DeleteFood(foodId: int):
        """delete a food from all menus"""

        menus = Menu.GetAll()
        
        for menu in menus:
            menu.removeFood(foodId) # delete if the menu has the food otherwise do nothing
            Menu.Update(menu.id, {"foods": menu.foods})


    #foods method


    def addFood(self, food) -> None:
        """add a food to menu
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            self.foods.append(food.id)

        if isinstance(food, int):
            if Food.Exists(food):
                self.foods.append(food)

        Menu.Update(self.id, {"foods" : self.foods})


    def removeFood(self, food) -> None:
        """remove a food from menu
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            id = food.id
        else:
            id = food

        if id in self.foods:
            self.foods.remove(id)
            Menu.Update(self.id, {"foods": self.foods})


    def getFoods(self) -> list['Food']:
        """get Food object for each food in menu"""

        foods = []

        for foodId in self.foods:
            food = Food.Get(foodId)
            
            if food:
                foods.append(food)

        return foods
