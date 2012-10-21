from PySide.QtGui import QTextEdit
from PySide.QtGui import QListWidget
from PySide.QtGui import QTabWidget
from PySide.QtGui import QAction
from PySide.QtGui import QMessageBox
from PySide.QtGui import QWidget
from PySide.QtCore import Qt
import pages

class TabView():
    def __init__(self, targetLayoutContainer):
        self.tabs = QTabWidget()
        targetLayoutContainer.addWidget(self.tabs)
    
    def set_logger(self, logger):
        self.logger = logger
        
    def show_page(self, page):
        widget = QWidget()
        pageWidget = pages.get_page_widget(page, widget)
        self.tabs.addTab(widget, page.label)
        
        
