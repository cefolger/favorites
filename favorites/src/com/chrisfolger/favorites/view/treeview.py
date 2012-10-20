from PySide.QtGui import QWidget
from PySide.QtGui import QDialog
from PySide.QtGui import QTextEdit
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QLabel
from PySide.QtGui import QTabWidget
from PySide.QtGui import QSizePolicy

class TreeView():
    def __init__(self, targetLayoutContainer):
        self.tree = QTreeWidget()
        targetLayoutContainer.addWidget(self.tree)
        
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
        
