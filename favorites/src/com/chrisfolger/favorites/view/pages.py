from PySide.QtGui import QDialog

class HtmlFavoritePage(QDialog):
    def __init__(self, parent=None):
        super(HtmlFavoritePage, self).__init__(parent)
        self.setWindowTitle("My Form")
