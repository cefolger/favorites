import sys
from PySide.QtCore import *
from PySide.QtGui import *
from view.mainview import MainWindow
from controller.mainviewcontroller import start 
 
 
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
form = MainWindow()
form.show()
start(form)
# Enter Qt application main loop
app.exec_()
sys.exit()