from enum import Enum
from tkinter import messagebox
import tkinter as tk

#message types: error / warning / success / info

class Messages:

    #list of messages
    Buffer = list()

    #select message type
    class Type(Enum):

        SUCCESS = ("SUCCESS", messagebox.showinfo)
        ERROR = ("ERROR", messagebox.showerror)
        INFO = ("INFO", messagebox.showinfo)
        WARNING = ("WARNING", messagebox.showwarning)


    class Message:

        def __init__(self, title, text, tkMethod):

            self.title = title
            self.text = text
            self.tkMethod = tkMethod

        def __str__(self):
            return self.title + ": " + self.text



    #add new message
    @staticmethod
    def push(type, text):

        if not isinstance(type, Messages.Type):
            return

        Messages.Buffer.append(Messages.Message(type.value[0], text, type.value[1]))


    #present messages
    @staticmethod
    def show():

        root = tk.Tk()
        root.withdraw()

        for message in Messages.Buffer:
            message.tkMethod( message.title, message.text )


        Messages.Buffer.clear()
