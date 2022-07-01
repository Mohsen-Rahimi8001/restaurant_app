from DataBase.Sqlite import Database
import sys
from PyQt5.QtWidgets import QApplication
from Window import Window


Database.Initialize()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())