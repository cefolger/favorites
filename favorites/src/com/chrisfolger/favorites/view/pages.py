from PySide.QtGui import QWidget
from PySide.QtGui import QLabel
from PySide.QtGui import QLineEdit
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QPushButton
from PySide.QtWebKit import QWebView

def get_page_widget(page, layout):
    if page.url:
        return HtmlFavoritePage(page, layout)

class HtmlFavoritePage():
    def __init__(self, page, layout):
        self.page = page
        
        container = QVBoxLayout()
        # actions section
        actionsContainer = QHBoxLayout()
        button = QPushButton('Save')
        actionsContainer.addWidget(QLabel('Link: '))
        actionsContainer.addWidget(QLineEdit(page.url))
        actionsContainer.addWidget(button)
        label = QLabel('<a href="' + page.url + '">Open Externally</a>')
        label.setOpenExternalLinks(True)
        actionsContainer.addWidget(label)
        container.addLayout(actionsContainer)
        # content section 
        view = QWebView()
        view.setUrl(page.url)
        container.addWidget(view)
        # properties section 
        
        layout.addLayout(container)
  
