from Models.Model import Model
from DataBase.Sqlite import Database

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
        data["foods"] = ""
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
            foods = row[1].split(),
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

        for date in rows:
            orders.append(Order(
                id=row[0],
                foods=row[1].split(),
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

        Database.Update(Order.TableName, Order.PrimaryKey, id)


    @staticmethod
    def Delete(id: int):
        """delete order"""

        if not Order.Exists(id):
            raise RuntimeError("Order does not exist")

        Database.Delete(Order.TableName, Order.PrimaryKey, id)



    



