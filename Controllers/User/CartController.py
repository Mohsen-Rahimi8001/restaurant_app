from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
from Models.Food import Food
from Controllers.AuthenticationController import Auth
from Lib.DateTools import DateTools
from Lib.Questions import Questions

class Cart:

    DeliverDate = False


    @staticmethod
    def ClearCart():

        user = Auth.GetUser()

        #return reserved foods to stock
        foods = user.getCartFoods()


        for food in foods:
            food.addToStock(1)

        #clear cart
        user.clearCart()
        Cart.DeliverDate = False


    @staticmethod
    def AddFood(food : Food):
        """add new food to cart"""

        user = Auth.GetUser()

        if food.stock > 0:
            user.addFoodToCart(food)
            food.reduceStock(1)
            return True
        else:
            Messages.push(Messages.Type.ERROR, f"all {food.title}(s) have been sold out")
            return False


    @staticmethod
    def CheckCartDeliverDateMatch(date : str) -> bool:

        if not Cart.DeliverDate or Cart.DeliverDate == date:
            return True
        return False


    @staticmethod
    def ChangeDeliverDate(date):

        if Cart.CheckCartDeliverDateMatch(date):
            return
        else:
            Cart.ClearCart()
            Cart.DeliverDate = date


    @staticmethod
    def ReserveFood(food : Food, menuDate : str):

        if not Cart.CheckCartDeliverDateMatch(menuDate):
            result = Questions.ask(Questions.Type.ASKYESNO, "there are already some foods from another menu in your cart\ndo you want to clear your cart to add this food?")
            if not result:
                return False

            Cart.ChangeDeliverDate(menuDate)

        result = Cart.AddFood(food)
        Cart.DeliverDate = menuDate
        return result



