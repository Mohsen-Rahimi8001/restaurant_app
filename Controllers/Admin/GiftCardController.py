from Models.GiftCard import GiftCard
from Models.Order import Order
from Models.User import User
from Lib.Email import Email
from Lib.Questions import Questions
from Lib.Messages import Messages
import datetime as dt
from Lib.DateTools import DateTools
import random



class GiftCardController:

    @staticmethod
    def Suggest() -> None:
        """Suggests a gift card for top 5 good users."""
        
        orders = Order.GetAll()
        
        users: dict[str, int] = {}

        for order in orders:
            user = User.Get(order.user_id)
            
            if user.email not in users:
                users[user.email] = order.getTotalPrice()
            else:
                users[user.email] += order.getTotalPrice()
        
        # sort user emails by their values and select 5 top users
        sorted_users = sorted(users.items(), key=lambda x: x[1], reverse=True)[-5:]

        # create a random gift card for good users
        giftCard = {
            "start_date" : (dt.datetime.now() + dt.timedelta(days=1)).strftime('%Y-%m-%d'),
            "expiration_date" : (dt.datetime.now() + dt.timedelta(days=8)).strftime('%Y-%m-%d'),
            "amount": random.randint(10, 50),
            "code": GiftCard.GetDefaultCode(),
            "sent": 0,
        }

        questionText = \
        f"""
        Do you want to send gift card:
        Amount: {giftCard['amount']} persent
        Code: {giftCard['start_date']}
        Start date: {giftCard['start_date']}
        Expiration date: {giftCard['expiration_date']}
        
        to the following users?
        """
        
        for user in sorted_users:
            questionText += f"{user[0]}) Total Sale: {user[1]}\n"

        if Questions.ask(Questions.Type.ASKYESNO, questionText):
            
            giftCard = GiftCard.Create(giftCard)
            
            for user, _ in sorted_users:
                GiftCardController.Send(User.GetUserByEmail(user), giftCard)
            
            giftCard = GiftCard.Get(giftCard)
            giftCard.sent = 1
            GiftCard.Update(giftCard.id, {'sent' : 1})
            
            Messages.push(Messages.Type.SUCCESS, "Gift card sent successfully.")
            Messages.show()


    @staticmethod
    def Send(user: User, giftCard):
        """Sends a gift card to a user. (It doesn't change the gift card to sent state)"""
        
        if isinstance(giftCard, int):
            giftCard = GiftCard.Get(giftCard)
            
            if not giftCard:
                raise ValueError("gift card does not exists")

        elif not isinstance(giftCard, GiftCard):
            raise TypeError("giftCard is not a GiftCard object")
        
        if giftCard.sent == 1:
            raise ValueError("gift card already sent")

        message = \
        f"""
        Hello Dear {user.first_name}

        You are one of our best customers.
        To appreciate you, dear customer, 
        we have prepared a discount offer for you.
        We hope you will enjoy it.
        
        _______________________________________
        This is the Gift Card:
        Amount: {giftCard.amount}%
        Code: {giftCard.code}
        Start date: {giftCard.start_date}
        Expiration date: {giftCard.expiration_date}
        """

        Email.Send(user.email, message)


    @staticmethod
    def SendToAll(giftCard):
        """Send the gift card to all the users"""

        if isinstance(giftCard, int):
            giftCard = GiftCard.Get(giftCard)
            
            if not giftCard:
                raise ValueError("gift card does not exists")

        elif not isinstance(giftCard, GiftCard):
            raise TypeError("giftCard is not a GiftCard object")
        
        if giftCard.sent == 1:
            raise ValueError("gift card already sent")

        users = User.GetAll()

        for user in users:

            message = \
            f"""
            Hello dear {user.first_name}
            We have prepared a discount offer for you.
            We hope you will enjoy it.
            
            This is the Gift Card:
            Amount: {giftCard.amount}%
            Code: {giftCard.code}
            Start date: {giftCard.start_date}
            Expiration date: {giftCard.expiration_date}
            """

            Email.Send(user.email, message)
        
        giftCard.sent = 1
        GiftCard.Update(giftCard.id, {'sent' : 1})


    @staticmethod
    def Evaluate(giftCardCode : str):

        #check for gift card exists
        if not GiftCard.ExistsByKey("code", giftCardCode):
            Messages.push(Messages.Type.WARNING, "gift card code is invalid")
            return False

        giftCard = GiftCard.GetByKey("code", giftCardCode)

        #check for today is after start date
        if DateTools.Compare(DateTools.GetToday(), giftCard.start_date) == 1:
            Messages.push(Messages.Type.WARNING, "gift card code is invalid")
            return False

        #check for expiration
        if DateTools.Compare(DateTools.GetToday(), giftCard.expiration_date) == -1:
            Messages.push(Messages.Type.WARNING, "gift card is expired")
            return False

        return amount