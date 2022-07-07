import textblob
from PyQt5 import QtGui, QtWidgets
import string


class SpellCorrecting:

    Word = ""

    @staticmethod
    def WordCorrect(word:str):
        """Returns the correct word"""
        word = textblob.Word(word)

        return word.correct()


    @staticmethod
    def SentenceCorrect(sentence:str):
        """Returns the correct sentence"""

        result = textblob.TextBlob(sentence)

        return str(result.correct())


    @staticmethod
    def KeyPressHandler(lineEdit:QtWidgets.QLineEdit):
        """When the space key is pressed the last word will be corrected"""

        if lineEdit.text() and lineEdit.text()[-1] in [" ", ".", ",", ";", ":", "!", "?", "-"]:
            correctedSentence = SpellCorrecting.SentenceCorrect(lineEdit.text())
        else:
            correctedSentence = lineEdit.text()
        
        lineEdit.setText(correctedSentence)
