from Models.Model import Model
from DataBase.Sqlite import Database
import json
from Models.Order import Order
from Models.Food import Food

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
    def Create(userData : dict):
        """create new user in database"""

        data = userData.copy()

        data["orders"] = ""
        data["cart"] = ""

        #set default role to user (1)
        if not "role" in data.keys():
            data["role"] = 1

        #set default value for image
        if not "image" in data.keys():
            data["image"] = "user_default.png"

        lastRow = Database.Create(User.TableName, data)
        return lastRow


    @staticmethod
    def Get(id: int) -> "User":
        """returns a user Model object representing a row in users table"""

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
            orders = json.loads(row[9]) if row[9] else [],
            cart = json.loads(row[10]) if row[10] else []
        )


    @staticmethod
    def GetAll() -> list:
        """get all users"""

        rows = Database.ReadAll(User.TableName)

        users = list()

        for row in rows:
            users.append(User(
                id = row[0],
                first_name = row[1],
                last_name = row[2],
                email = row[3],
                phone_number = row[4],
                social_number = row[5],
                image = row[6],
                password = row[7],
                role = row[8],
                orders=json.loads(row[9]) if row[9] else [],
                cart=json.loads(row[10]) if row[10] else []
        ))

        return users


    @staticmethod
    def Exists(id: int):
        """check if a user exists in database or not"""
        return Database.Exists(User.TableName, User.PrimaryKey, id)


    @staticmethod
    def Update(id: int, userData : dict):
        """update user"""

        if not User.Exists(id):
            raise RuntimeError("user does not exists")

        data = userData.copy()

        #update the role is forbidden
        if "role" in data.keys():
            data.pop("role")

        #can't update id
        if "id" in data.keys():
            data.pop("id")

        #convert lists to json
        if "orders" in data.keys():
            data["orders"] = json.dumps(data["orders"])

        if "cart" in data.keys():
            data["cart"] = json.dumps(data["cart"])


        Database.Update(User.TableName, User.PrimaryKey, id, data)


    @staticmethod
    def Delete(id: int):
        """delete user"""

        if not User.Exists(id):
            raise RuntimeError("user does not exists")

        Database.Delete(User.TableName, User.PrimaryKey, id)


    @staticmethod
    def SearchByEmail(email : str):
        """check if an email exists in database or not"""
        return Database.Exists(User.TableName, "email", email)





    #cart methods

    def addFoodToCart(self, food) -> None:
        """add a food to user cart
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            self.cart.append(food.id)

        if isinstance(food, int):
            if Food.Exists(food):
                self.cart.append(food)

        User.Update(self.id, {"cart": self.cart})


    def removeFoodFromCart(self, food) -> None:
        """remove a food from user cart
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            id = food.id
        else:
            id = food

        if id in self.cart:
            self.cart.remove(id)
            User.Update(self.id, {"cart": self.cart})


    def getCartFoods(self) -> list:
        """get Food object for each food in user cart"""

        foods = []

        for foodId in self.cart:
            foods.append(Food.Get(foodId))

        return foods


