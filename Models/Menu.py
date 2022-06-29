from Models.Model import Model
import json
from Models.Food import Food

class Menu(Model):

    TableName = "menus"
    PrimaryKey = "id"

    def __init__(self, id : int, title : str, foods : list, date : str):

        super(Menu, self).__init__(id)
        self.title : str = title
        self.foods : list = foods
        self.date : str = date



    @staticmethod
    def Create(data):
        """create new menu in database"""

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
            foods = json.loads(row[2]),
            date = row[3]
        )


    @staticmethod
    def GetAll():
        """get all orders"""

        rows = Database.ReadAll(Menu.TableName)

        menus = list()

        for row in rows:
            menus.append(Menu(
                id=row[0],
                title=row[1],
                foods=json.loads(row[2]),
                date=row[3]
            ))

        return menus


    @staticmethod
    def Exists(id : int):
        """check if a menu exists in database or not"""

        return Database.Exists(Menu.TableName, Menu.PrimaryKey, id)


    @staticmethod
    def Update(id : int, data):
        """update menu"""

        if not Menu.Exists(id):
            raise RuntimeError("menu does not exist")

        if "id" in data.keys():
            data.pop("id")

        if "foods" in data.keys():
            data["foods"] = json.dumps(data["foods"])

        Database.Update(Menu.TableName, Menu.PrimaryKey, id, data)



    @staticmethod
    def Delete(id : int):
        """delete menu"""

        if not Menu.Exists(id):
            raise RuntimeError("menu does not exist")

        Database.Delete(Menu.TableName, Menu.PrimaryKey, id)