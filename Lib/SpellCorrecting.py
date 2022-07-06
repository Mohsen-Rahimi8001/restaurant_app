import textblob
from PyQt5 import QtGui, QtWidgets


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
    def KeyPressHandler(event:QtGui.QKeyEvent, lineEdit:QtWidgets.QLineEdit):
        """When the space key is pressed the last word will be corrected"""
        
        if event.key() == 16777219: # back space
            SpellCorrecting.Word = SpellCorrecting.Word[:-1]
            lineEdit.setText(lineEdit.text()[:-1])
            return

        if event.text() == " ":
            if SpellCorrecting.Word != "":
                correctedWord = SpellCorrecting.WordCorrect(SpellCorrecting.Word)
                lineEdit.setText(lineEdit.text()[:-len(correctedWord)] + correctedWord + " ")
                SpellCorrecting.Word = ""
                return

        SpellCorrecting.Word += event.text()
        lineEdit.insert(event.text())
