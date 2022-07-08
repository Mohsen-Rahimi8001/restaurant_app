from Controllers.Validation import UserValidator
from Lib.Messages import Messages
from Models.User import User
from Models.Food import Food
from Controllers.AuthenticationController import Auth
from Lib.DateTools import DateTools
from Lib.Questions import Questions
from Controllers.Admin.GiftCardController import GiftCardController
import base64
from datetime import datetime
from Controllers.Validation import PaymentValidator
from Controllers.User.CartController import Cart
from Models.Order import Order

class OrderController:

    @staticmethod
    def GenerateRefNum() -> str:
        return str(datetime.now().strftime("%S%H%M%m%d%Y%f"))


    @staticmethod
    def ConfirmPayment(paymentMethod, accountNumber):

        #validate payment method
        if paymentMethod not in [0,1]:
            Messages.push(Messages.Type.ERROR, "select payment method")
            return False

        #validate account number
        if paymentMethod == 0:
            if not PaymentValidator.ValidateAccountNumber(accountNumber):
                return False

        user = Auth.GetUser()

        data = {
            "foods" : user.cart.copy(),
            "order_date" : DateTools.GetToday(),
            "deliver_date" : Cart.DeliverDate,
            "payment_method" : paymentMethod,
            "reference_number" : OrderController.GenerateRefNum(),
            "account_number" : accountNumber,
            "user_id" : user.id,
        }

        result = Order.Create(data)

        return result

