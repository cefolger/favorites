from PySide.QtGui import QDialog
from PySide.QtGui import QLineEdit
from PySide.QtGui import QPushButton
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QVBoxLayout
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QTabWidget
from pages import HtmlFavoritePage

class MainView(QDialog):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.setWindowTitle("My Form")
        
        # Create widgets
        self.button = QPushButton('hello there')
        self.tree = QTreeWidget()
        self.tabs = QTabWidget()
        self.tabs.addTab(HtmlFavoritePage(), 'foo')
        self.tabs.addTab(HtmlFavoritePage(), 'bar')
        
        container = QVBoxLayout()
        topContainer = QHBoxLayout()
        bottomContainer = QHBoxLayout()
        
        container.addLayout(topContainer)
        container.addLayout(bottomContainer)
        topContainer.addWidget(self.tree)
        topContainer.addWidget(self.tabs)
        
        
        # Set dialog layout
        self.setLayout(container)

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