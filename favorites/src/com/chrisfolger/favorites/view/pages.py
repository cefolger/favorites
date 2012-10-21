from PySide.QtGui import QWidget
from PySide.QtGui import QLabel
from PySide.QtGui import QLineEdit
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QPushButton
from PySide.QtGui import QMessageBox
from PySide.QtWebKit import QWebView

def get_page_widget(page, layout, parent):
    if page.url:
        return HtmlFavoritePage(page, layout, parent)

# for some reason this doesn't get called when inside HtmlFavoritePage?
def save_clicked(pageWidget):
    if pageWidget.page.url == pageWidget.linkText.text():
        return
    
    pageWidget.page.url = pageWidget.linkText.text()
    pageWidget.view.setUrl(pageWidget.page.url)
    pageWidget.parent.save_page(pageWidget.page)

class HtmlFavoritePage():
    def __init__(self, page, layout, parent):
        self.page = page
        self.parent = parent
        
        container = QVBoxLayout()
        # actions section
        actionsContainer = QHBoxLayout()
        
        self.saveButton = QPushButton('Save')
        self.saveButton.clicked.connect(lambda: save_clicked(self))
                
        actionsContainer.addWidget(QLabel('Link: '))
        self.linkText = QLineEdit(page.url)
        
        label = QLabel('<a href="' + page.url + '">Open Externally</a>')
        label.setOpenExternalLinks(True)
        
        actionsContainer.addWidget(self.linkText)
        actionsContainer.addWidget(self.saveButton)
        actionsContainer.addWidget(label)
        container.addLayout(actionsContainer)
        
        # content 
        self.view = QWebView()
        self.view.setUrl(page.url)
        container.addWidget(self.view)
        layout.addLayout(container)        
    
