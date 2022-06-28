from Models.Model import Model
from DataBase.Sqlite import Database
import json

class User(Model):

    TableName = "users"
    PrimaryKey = "id"


    def __init__(self, id: int, first_name : str, last_name : str, email : str, phone_number : str, social_number : str,
                 image : str, password : str, role : int, orders : list, cart : list) -> None:

        super(User, self).__init__(id)
        self.first_name : str = first_name
        self.last_name : str = last_name
        self.email : str = email
        self.phone_number : str = phone_number
        self.social_number : str = social_number
        self.image : str = image
        self.password : str = password
        self.role : int = role
        self.orders : list = orders
        self.cart : list = cart


    @staticmethod
    def Create(data : dict):

        data["orders"] = ""
        data["cart"] = ""

        #set default role to user (1)
        if not "role" in data.keys():
            data["role"] = 1

        #set default value for image
        if not "image" in data.keys():
            data["image"] = "default_user.png"

        lastRow = Database.Create(User.TableName, data)
        return lastRow


    @staticmethod
    def Get(id: int):

        if not User.Exists(id):
            raise RuntimeError("user does not exists")

        row : list = Database.Read(User.TableName, User.PrimaryKey, id)[0]

        return User(
            id = row[0],
            first_name = row[1],
            last_name = row[2],
            email = row[3],
            phone_number = row[4],
            social_number = row[5],
            image = row[6],
            password = row[7],
            role = row[8],
            orders = json.loads(row[9]),
            cart = json.loads(row[10])
        )


    @staticmethod
    def Exists(id: int):
        return Database.Exists(User.TableName, User.PrimaryKey, id)


    @staticmethod
    def Update(id: int, data : dict):

        if not User.Exists(id):
            raise RuntimeError("user does not exists")

        #update the role is forbidden
        if "role" in data.keys():
            data.pop("role")

        #can't update id
        if "id" in data.keys():
            data.pop("id")

        #convert lists to json
        if "orders" in data.keys():
            data["orders"] = json.dumps(data["order"])

        if "cart" in data.keys():
            data["cart"] = json.dumps(data["cart"])


        Database.Update(User.TableName, User.PrimaryKey, id, data)


    @staticmethod
    def Delete(id: int):

        if not User.Exists(id):
            raise RuntimeError("user does not exists")

        Database.Delete(User.TableName, User.PrimaryKey, id)






