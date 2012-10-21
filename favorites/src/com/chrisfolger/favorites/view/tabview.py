from PySide.QtGui import QTextEdit
from PySide.QtGui import QListWidget
from PySide.QtGui import QTabWidget
from PySide.QtGui import QAction
from PySide.QtGui import QMessageBox
from PySide.QtGui import QWidget
from PySide.QtGui import QHBoxLayout
from PySide.QtCore import Qt
import pages
import controller.tabcontroller as controller

class TabView():
    def __init__(self, targetLayoutContainer):
        self.tabs = QTabWidget()
        targetLayoutContainer.addWidget(self.tabs, 10)
    
    def set_logger(self, logger):
        self.logger = logger
        
    def show_page(self, page):
        print 'page is ' + page.item.name
        widget = QWidget()
        
        layout = QHBoxLayout()
        widget.setLayout(layout)
        
        pageWidget = pages.get_page_widget(page, layout, self)
        self.tabs.insertTab(0, widget, page.label)
        self.tabs.setCurrentIndex(0)
        
    def save_page(self, page):
        self.logger.info(__name__, 'save_page', page.description())
        controller.save_page(page)
        
    def clear(self):
        self.tabs.clear()
        print 'cleared'
        
        
