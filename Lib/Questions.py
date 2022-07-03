from enum import Enum
from tkinter import messagebox
import tkinter as tk

# Questions types: askyesno / askokcancel

class Questions:


    #select ask type
    class Type(Enum):

        ASKYESNO = ("Are you sure?", messagebox.askyesno)
        ASKOKCANCEL = ("ATTENTION", messagebox.askokcancel)


    class Question:

        def __init__(self, title, text, tkMethod):

            self.title = title
            self.text = text
            self.tkMethod = tkMethod

        def __str__(self):
            return self.title + ": " + self.text


    @staticmethod
    def ask(type, text):
        """ask a message and return the result."""

        if not isinstance(type, Questions.Type):
            return

        # create the ask message
        message = Questions.Question(type.value[0], text, type.value[1])
        
        root = tk.Tk()
        root.withdraw()

        # show the ask message
        return message.tkMethod(message.title, message.text)

