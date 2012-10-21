from PySide.QtGui import QWidget
from PySide.QtGui import QLabel

def get_page_widget(page, layout):
    if page.url:
        return HtmlFavoritePage(page, layout)

class HtmlFavoritePage():
    def __init__(self, page, layout):
        self.page = page
        label = QLabel('<a href="' + page.url + '">Click here to open the URL</a>')
        label.setOpenExternalLinks(True)
        layout.addWidget(label)
        label.show()
  
