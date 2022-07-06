import os
import dotenv
import telegram.ext as tg
from TelegramBot.InitBot import InitHandlers
from TelegramBot.Login.Auth import BotAuth
from TelegramBot.Chat.Chat import BotChat



class Telegram:

    @staticmethod
    def get_handlers():
        """get all handlers"""
        
        # put handlers in here
        handlers = [
            tg.CommandHandler("start", InitHandlers.start_command),
            tg.CommandHandler("help", InitHandlers.help_command),
            tg.CommandHandler("login", BotAuth.login_command),
            tg.CommandHandler("chat", BotChat.start_chat_command),
            tg.CommandHandler("stop_chat", BotChat.stop_chat_command),
            tg.CommandHandler("send", BotChat.send_message),
            tg.CommandHandler("logout", BotAuth.logout_command),
        ]

        return handlers


    @staticmethod
    def start():
        """start telegram bot"""

        # get bot token from .env file
        dotenv.load_dotenv(dotenv.find_dotenv())
        
        #get bot token
        token = os.environ.get("API_KEY")

        #create bot
        bot = tg.Updater(token)

        #get dispatcher
        dispatcher = bot.dispatcher

        #get handlers
        handlers = Telegram.get_handlers()

        #add handlers to dispatcher
        for handler in handlers:
            dispatcher.add_handler(handler)

        print('Telegram bot started to work!')

        #start bot
        bot.start_polling(1) # one second delay
