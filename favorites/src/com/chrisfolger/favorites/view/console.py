from PySide.QtGui import QWidget
from PySide.QtGui import QDialog
from PySide.QtGui import QTextEdit
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QLabel

class Console(QWidget):
    def __init__(self, parent=None):
        super(Console, self).__init__()
        self.textarea = QTreeWidget()
        
        layout = QVBoxLayout(self)
        layout.addChildWidget(self.textarea)
        self.setLayout(layout)
        self.show()