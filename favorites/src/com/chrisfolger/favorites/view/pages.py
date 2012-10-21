from PySide.QtGui import QWidget

def get_page_widget(page, target):
    if page.url:
        return HtmlFavoritePage(target)

class HtmlFavoritePage():
    def __init__(self, targetWidget):
        pass
  
