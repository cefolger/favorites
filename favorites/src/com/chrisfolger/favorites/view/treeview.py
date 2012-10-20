from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QAction
from PySide.QtCore import Qt

class TreeView():
    def __init__(self, targetLayoutContainer):
        self.tree = QTreeWidget()
        self.tree.addAction(QAction('Add nested favorite', self.tree, triggered=self.add_child))
        self.tree.setContextMenuPolicy(Qt.ActionsContextMenu)
        
        
        targetLayoutContainer.addWidget(self.tree)
        
    def add_child(self):
        item = self.tree.currentItem()
        
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
        
