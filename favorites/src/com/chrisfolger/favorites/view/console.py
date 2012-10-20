from PySide.QtGui import QDialog

class Console(QDialog):
    def __init__(self, parent=None):
        super(Console, self).__init__(parent)
        self.setWindowTitle("Logger")