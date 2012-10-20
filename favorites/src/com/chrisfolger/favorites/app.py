import sys
from PySide.QtCore import *
from PySide.QtGui import *
from view.mainview import MainView
 
 
# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
form = MainView()
form.show()
# Enter Qt application main loop
app.exec_()
sys.exit()