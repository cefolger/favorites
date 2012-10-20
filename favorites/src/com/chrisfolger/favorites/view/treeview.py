from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QAction
from PySide.QtCore import Qt
from controller.mainviewcontroller import add_child

class TreeView():
    def __init__(self, targetLayoutContainer):
        self.tree = QTreeWidget()
        self.tree.addAction(QAction('Add nested favorite', self.tree, triggered=self.add_child))
        self.tree.setContextMenuPolicy(Qt.ActionsContextMenu)
        targetLayoutContainer.addWidget(self.tree)
        
    def add_child(self):
        item = self.tree.currentItem()
        print item.data(1, Qt.ItemDataRole.EditRole).getFullPath()
        add_child(item.data(1, Qt.ItemDataRole.EditRole))
        
    def set_favorites(self, favoritesRoot):
        item = QTreeWidgetItem()
        item.setText(0, favoritesRoot.label)
        item.setData(1,Qt.ItemDataRole.EditRole, favoritesRoot)
        
        self.tree.addTopLevelItem(item)
        self.add_children(favoritesRoot, item)
    
    def add_children(self, node, item):
        for child in node.children:
            childItem = QTreeWidgetItem()
            childItem.setText(0, child.label)
            childItem.setData(1,Qt.ItemDataRole.EditRole, child)
            item.addChild(childItem)
            
            self.add_children(child, childItem)
        
