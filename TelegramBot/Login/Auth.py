from Controllers.AuthenticationController import Auth
from Constants.RegExValidations import Patterns
import re


class BotAuth:

    @staticmethod
    def login_command(update, command):
        """login command"""
        
        # get the email and password
        text = str(update.message.text)
        
        try:
            email = text.split()[1]
            password = text.split()[2]
        except IndexError:
            update.message.reply_text("Please enter your email and password! like this: /login <email> <password>")
            return

        # check if the email is valid
        if not re.match(Patterns.EMAIL.value, email):
            update.message.reply_text("Please enter a valid email!, use this format: <email>@<domain>.<tld>")
            return

        if Auth.Login({ "email": email, "password": password }):
            update.message.reply_text(f"Hello. You are logged in!")
        else:
            update.message.reply_text("Wrong email or password!")
    
    
    @staticmethod
    def logout_command(update, command):
        """logout command"""
        Auth.LogOut()
        update.message.reply_text("You are logged out!")
