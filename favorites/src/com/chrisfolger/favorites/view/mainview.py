from PySide.QtGui import QDialog
from PySide.QtGui import QPushButton
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QFileDialog
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QMainWindow
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QMenu
from PySide.QtGui import QMenuBar
from PySide.QtGui import QTabWidget
from PySide.QtGui import QLayout
from PySide.QtGui import QWidget

from pages import HtmlFavoritePage
from console import Console
from controller.mainviewcontroller import new_repository
from controller.mainviewcontroller import open_repository

    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)

        fileMenu = self.menuBar().addMenu('File')
        newRepository = fileMenu.addAction('New Repository')
        openRepository = fileMenu.addAction('Open Repository')
        newRepository.triggered.connect(self.create_new_repository)
        openRepository.triggered.connect(self.open_repository)
        
        self.button = QPushButton('hello there')
        self.tree = QTreeWidget()
        self.tabs = QTabWidget()
        self.tabs.addTab(HtmlFavoritePage(), 'foo')
        self.tabs.addTab(HtmlFavoritePage(), 'bar')
        
        container = QVBoxLayout()
        menuContainer = QHBoxLayout()
        topContainer = QHBoxLayout()
        bottomContainer = QHBoxLayout()
        self.console = Console(bottomContainer)

        container.addLayout(menuContainer, 0)
        container.addLayout(topContainer, 5)
        container.addLayout(bottomContainer, 3)
        topContainer.addWidget(self.tree)
        topContainer.addWidget(self.tabs)
        
        widget.setLayout(container)
    
    def set_favorites(self, favoritesRoot):
        item = QTreeWidgetItem()
        item.setText(0, favoritesRoot.label)
        self.tree.addTopLevelItem(item)
        self.add_children(favoritesRoot, item)
    
    def add_children(self, node, item):
        for child in node.children:
            childItem = QTreeWidgetItem()
            childItem.setText(0, child.label)
            item.addChild(childItem)
            
            self.add_children(child, childItem)
            
    def get_logger(self):
        return self.console
    
    def create_new_repository(self):
        directory = QFileDialog.getExistingDirectory()
        new_repository(directory)
        self.currentRepository = directory 
        
    def open_repository(self):
        directory = QFileDialog.getExistingDirectory()
        open_repository(directory)
        self.currentRepository = directory