from Controllers.AuthenticationController import Auth
from Models.Message import Message
import datetime as dt


class BotChat:

    Started = False

    @staticmethod
    def SendMessage(update, message:Message):
        """sends the message in the write format"""

        update.message.reply_text(f"[{message.admin_email}_{message.datetime}]: {message.message}")


    @staticmethod
    def check_for_credentials():
        """check if the user is logged in and has the admin credentials."""
        if Auth.IsUserLoggedIN() and Auth.CheckAdminCredentials():
            return True
        else:
            return False


    @staticmethod
    def start_chat_command(update, context):
        """starts chat"""
        
        if not BotChat.check_for_credentials():
            update.message.reply_text("You are not logged in or you don't have admin credentials!")
            return

        BotChat.Started = True
        update.message.reply_text("Chat Started! you can send any message you want!!!")
        
        messages = Message.GetAll()

        for message in messages:
            BotChat.SendMessage(update, message)


    @staticmethod
    def stop_chat_command(update, context):
        """stops chat"""
        
        BotChat.Started = False
        update.message.reply_text("Chat Stopped!")


    @staticmethod
    def send_message(update, context):
        """sends message"""
        
        text = str(update.message.text)

        # get the chat content
        try:
            messageText = ' '.join(text.split()[1:])
        except IndexError:
            update.message.reply_text("Please enter your message like this: /send <message>")
            return

        if not BotChat.Started:
            update.message.reply_text("Chat is not started!")
            return

        user = Auth.GetUser()

        messageId = Message.Create({
            "admin_email": user.email,
            "message": messageText,
            "datetime": dt.datetime.now().strftime(Message.DateTimePattern)
        })

        BotChat.SendMessage(update, Message.Get(messageId))
