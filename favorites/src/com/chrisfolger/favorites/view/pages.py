from PySide.QtGui import QWidget

def get_page_widget(page):
    if page.url:
        return HtmlFavoritePage()

class HtmlFavoritePage():
    def __init__(self, targetLayoutContainer):
        self.widget = QWidget()
        targetLayoutContainer.addWidget(self.widget)
        
  
