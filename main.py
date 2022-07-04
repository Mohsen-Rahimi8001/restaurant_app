from Initialize import Initialize
import sys
from PyQt5.QtWidgets import QApplication
from Window import Window


Initialize.Run()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())