from PySide.QtGui import QWidget
from PySide.QtGui import QDialog
from PySide.QtGui import QTextEdit
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QLabel
from PySide.QtGui import QTabWidget

class Console(QWidget):
    def __init__(self, parent=None):
        super(Console, self).__init__()
        self.textarea = QTextEdit()
        self.textarea.setSizePolicy()

        layout = QHBoxLayout(self)
        layout.addChildWidget(self.textarea)
        self.setLayout(layout)
