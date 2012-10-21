from PySide.QtGui import QDialog
from PySide.QtGui import QPushButton
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QFileDialog
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QMainWindow
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QMessageBox
from PySide.QtGui import QMenu
from PySide.QtGui import QMenuBar
from PySide.QtGui import QTabWidget
from PySide.QtGui import QLayout
from PySide.QtGui import QWidget

from pages import HtmlFavoritePage
from console import Console
from treeview import TreeView
from tabview import TabView
from controller.mainviewcontroller import new_repository
from controller.mainviewcontroller import open_repository
from controller.mainviewcontroller import rollback

    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)

        fileMenu = self.menuBar().addMenu('File')
        newRepository = fileMenu.addAction('New Repository')
        openRepository = fileMenu.addAction('Open Repository')
        rollbackRepository = fileMenu.addAction('Discard last commit')
        
        newRepository.triggered.connect(self.create_new_repository)
        openRepository.triggered.connect(self.open_repository)
        rollbackRepository.triggered.connect(self.discard_last_commit)
        
        self.button = QPushButton('hello there')
        
        container = QVBoxLayout()
        menuContainer = QHBoxLayout()
        topContainer = QHBoxLayout()
        bottomContainer = QHBoxLayout()
        self.console = Console(bottomContainer)
        self.tree = TreeView(topContainer)

        container.addLayout(menuContainer, 0)
        container.addLayout(topContainer, 5)
        container.addLayout(bottomContainer, 3)
        self.tabs = TabView(topContainer)
        
        widget.setLayout(container)
    
    def set_favorites(self, favoritesRoot):
        self.tabs.clear()
        self.tree.set_favorites(favoritesRoot)
            
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
        
    def discard_last_commit(self):
        if QMessageBox.warning(self, 'Discard last commit?', 'this will do a hard reset to the previous commit, so the current one will be lost', QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            rollback()
