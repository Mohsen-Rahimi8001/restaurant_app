from Models.Model import Model
from DataBase.Sqlite import Database
from Models.Food import Food
import json

class Order(Model):


    TableName = "orders"
    PrimaryKey = "id"


    def __init__(self, id : int, foods : list, date : str, paid : bool, reference_number : str, delivered : bool,
                 user_id : int, account_number : str):

        super(Order, self).__init__(id)
        self.foods : list = foods
        self.date : str = date
        self.paid : bool = paid
        self.reference_number : str = reference_number
        self.delivered : bool = delivered
        self.user_id : int = user_id
        self.account_number : str = account_number


    @staticmethod
    def Create(data : dict):
        """create new order in database"""

        #initial conditions
        data["foods"] = json.dumps(data["foods"])
        data["paid"] = 0
        data["reference_number"] = ""
        data["delivered"] = 0
        data["account_number"] = ""

        return Database.Create(Order.TableName, data)


    @staticmethod
    def Get(id: int) -> "Order":
        """returns an Order Model object representing a row in orders table with"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        row  : list = Database.Read(Order.TableName, Order.PrimaryKey, id)[0]

        return Order(
            id = row[0],
            foods = json.loads(row[1]),
            date = row[2],
            paid = row[3],
            reference_number = row[4],
            delivered = row[5],
            user_id = row[6],
            account_number = row[7],
        )


    @staticmethod
    def GetAll() -> list:
        """get all orders"""

        rows = Database.ReadAll(Order.TableName)

        orders = list()

        for row in rows:
            orders.append(Order(
                id=row[0],
                foods=json.loads(row[1]),
                date=row[2],
                paid=row[3],
                reference_number=row[4],
                delivered=row[5],
                user_id=row[6],
                account_number=row[7],
            ))

        return orders


    @staticmethod
    def Exists(id: int):
        """check if an order exists in database or not"""

        return Database.Exists(Order.TableName, Order.PrimaryKey, id)


    @staticmethod
    def Update(id: int, data : dict):
        """update order"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        #can't update id
        if "id" in data.keys():
            data.pop("id")

        if "foods" in data.keys():
            data["foods"] = json.dumps(data["foods"])

        Database.Update(Order.TableName, Order.PrimaryKey, id, data)


    @staticmethod
    def Delete(id: int):
        """delete order"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        Database.Delete(Order.TableName, Order.PrimaryKey, id)



    #work with foods

    def addFood(self, food) -> None:
        """add a food to order
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            self.foods.append(food.id)

        if isinstance(food, int):
            if Food.Exists(food):
                self.foods.append(food)

        Order.Update(self.id, {"foods" : self.foods})


    def removeFood(self, food) -> None:
        """remove a food from order
            :param food can be Food object or food table id
        """

        if isinstance(food, Food):
            id = food.id
        else:
            id = food

        if id in self.foods:
            self.foods.remove(id)
            Order.Update(self.id, {"foods": self.foods})


    def getFoods(self) -> list:
        """get Food object for each food in order"""

        foods = []

        for foodId in self.foods:
            foods.append(Food.Get(foodId))

        return foods



    #properties

    foods = property(fget = getFoods)

    def getUserId(self):
        return self.__user_id

    def setUserId(self, id):

        if not isinstance(id, int) or not id >= 0:
            raise TypeError("invalid user_id")

        self.__user_id = id

    user_id = property(fget = getUserId, fset = setUserId)

    




