from Models.Model import Model
from DataBase.Sqlite import Database
from Models.Food import Food
import json

class Order(Model):


    TableName = "orders"
    PrimaryKey = "id"


    def __init__(self, id : int, foods : list, order_date : str, deliver_date : str, payment_method : int, reference_number : str,
                 account_number : str, delivered : bool, confirmed : bool , user_id : int):

        super(Order, self).__init__(id)
        self.foods : list = foods
        self.order_date : str = order_date
        self.deliver_date : str = order_date
        self.payment_method : int = payment_method
        self.reference_number : str = reference_number
        self.account_number: str = account_number
        self.delivered : bool = delivered
        self.confirmed : bool = confirmed
        self.user_id : int = user_id




    @staticmethod
    def Create(order_data : dict):
        """create new order in database"""

        data = order_data.copy()

        #initial conditions
        data["foods"] = json.dumps(data["foods"])
        data["delivered"] = 0
        data["confirmed"] = 0

        return Database.Create(Order.TableName, data)


    @staticmethod
    def Get(id: int) -> "Order":
        """returns an Order Model object representing a row in orders table with"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        row : list = Database.Read(Order.TableName, Order.PrimaryKey, id)[0]

        return Order(
            id = row[0],
            foods = json.loads(row[1]) if row[1] else list(),
            order_date = row[2],
            deliver_date = row[3],
            payment_method = int(row[4]),
            reference_number = row[5],
            account_number = row[6],
            delivered = bool(row[7]),
            confirmed = bool(row[8]),
            user_id = int(row[9])
        )


    @staticmethod
    def GetAll() -> list['Order']:
        """get all orders"""

        rows = Database.ReadAll(Order.TableName)

        orders = list()

        for row in rows:
            orders.append(Order(
                id=row[0],
                foods=json.loads(row[1]) if row[1] else list(),
                order_date=row[2],
                deliver_date=row[3],
                payment_method=int(row[4]),
                reference_number=row[5],
                account_number=row[6],
                delivered=bool(row[7]),
                confirmed=bool(row[8]),
                user_id = int(row[9])
            ))

        return orders


    @staticmethod
    def Exists(id: int):
        """check if an order exists in database or not"""

        return Database.Exists(Order.TableName, Order.PrimaryKey, id)


    @staticmethod
    def Update(id: int, order_data : dict):
        """update order"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        data = order_data.copy()

        #can't update id
        if "id" in data.keys():
            data.pop("id")

        #convert booleans to int
        if "delivered" in data.keys():
            data["delivered"] = 1 if data["delivered"] else 0

        if "confirmed" in data.keys():
            data["confirmed"] = 1 if data["confirmed"] else 0

        #converts lists to string
        if "foods" in data.keys():
            data["foods"] = json.dumps(data["foods"])

        Database.Update(Order.TableName, Order.PrimaryKey, id, data)


    @staticmethod
    def Delete(id: int):
        """delete order"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        Database.Delete(Order.TableName, Order.PrimaryKey, id)



    def deliver(self):
        """set an order state to delivered"""

        self.delivered = True
        Order.Update(self.id, {"delivered" : True})


    def confirm(self):
        """confirm an order"""

        self.confirmed = True
        Order.Update(self.id, {"confirmed" : True})



    #work with foods

    def addFood(self, food) -> None:
        """add food to order
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


    def getFoods(self) -> list['Food']:
        """get Food object for each food in order"""

        foods = []

        for foodId in self.foods:
            food = Food.Get(foodId)
            
            if food:     
                foods.append(Food.Get(foodId))

        return foods


    def getTotalInterest(self):
        """get total interest for order"""

        total = 0

        for food in self.getFoods():
            total += food.sale_price - food.fixed_price

        return total


    def getTotalPrice(self):
        """get total price for order"""

        total = 0

        for food in self.getFoods():
            total += food.sale_price

        return total


    #properties

    def getUserId(self):
        return self.__user_id

    def setUserId(self, id):

        if not isinstance(id, int) or not id >= 0:
            raise TypeError("invalid user_id")

        self.__user_id = id

    user_id = property(fget = getUserId, fset = setUserId)

    


    def getPrice(self):

        foods = self.getFoods()

        price = 0

        for food in foods:
            price += food.sale_price

        return price


    def countFood(self, food) -> int:
        """returns count of given food in foods"""

        if isinstance(food, Food):
            id = food.id
        else:
            id = food

        return self.foods.count(id)


    def getTotalPriceOfFood(self, food):

        return self.countFood(food) * food.sale_price



