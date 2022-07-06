class InitHandlers:

    @staticmethod
    def start_command(update, context):
        """start handler"""
        update.message.reply_text("Hello, welcome to our restaurant bot,\nto show commands send /help")

    @staticmethod
    def help_command(update, context):
        """help handler"""
        update.message.reply_text(
            "To login send /login <email> <password>\n"
            "To logout send /logout\n"
            "To start chat send /chat\n"
            "To stop chat send /stop_chat\n"
            "To send message send /send <message>\n"
            )

