from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from PySide.QtGui import QAction
from PySide.QtGui import QInputDialog
from PySide.QtGui import QMessageBox
from PySide.QtCore import Qt
from controller.mainviewcontroller import add_child
from controller.mainviewcontroller import save
from controller.mainviewcontroller import delete
import controller.mainviewcontroller as controller
import pages

class TreeView():
    def __init__(self, targetLayoutContainer):
        self.tree = QTreeWidget()
        self.tree.addAction(QAction('Add nested favorite', self.tree, triggered=self.add_child))
        self.tree.addAction(QAction('Edit Title', self.tree, triggered=self.edit_title))
        self.tree.addAction(QAction('HTML page', self.tree, triggered=self.create_html_page))
        self.tree.addAction(QAction('Delete', self.tree, triggered=self.delete))
        self.tree.setContextMenuPolicy(Qt.ActionsContextMenu)
        targetLayoutContainer.addWidget(self.tree)
        
    def add_child(self):
        item = self.tree.currentItem()
        print item.data(1, Qt.ItemDataRole.EditRole).getFullPath()
        newItem = add_child(item.data(1, Qt.ItemDataRole.EditRole))
        
        newChildNode = QTreeWidgetItem()
        newChildNode.setText(0, newItem.label)
        newChildNode.setData(1, Qt.ItemDataRole.EditRole, newItem)
        item.addChild(newChildNode)
        
    def get_item(self, node):
        return node.data(1, Qt.ItemDataRole.EditRole)
        
    def set_favorites(self, favoritesRoot):
        self.tree.clear()
        
        item = QTreeWidgetItem()
        item.setText(0, favoritesRoot.label)
        item.setData(1,Qt.ItemDataRole.EditRole, favoritesRoot)
        
        self.tree.addTopLevelItem(item)
        self.add_children(favoritesRoot, item)
    
    def edit_title(self):
        newTitle, result = QInputDialog.getText(None, 'new title', 'enter a new title')
        
        if not result:
            return
            
        item = self.get_item(self.tree.currentItem())
        item.label = newTitle
        save(item, newTitle)
        self.tree.currentItem().setText(0, item.label)
    
    def create_html_page(self):
        item = self.get_item(self.tree.currentItem())
        
        page = None
        
        if item.page == None:
            page = item.add_html_page()
            save(item, page=page)
        else:
            page = item.add_html_page()
        
        self.show_page(page)
    
    def add_children(self, node, item):
        for child in node.children:
            childItem = QTreeWidgetItem()
            childItem.setText(0, child.label)
            childItem.setData(1,Qt.ItemDataRole.EditRole, child)
            item.addChild(childItem)
            
            self.add_children(child, childItem)
            
    def delete(self):
        if(self.get_item(self.tree.currentItem()).parent == None):
            QMessageBox.warning(None, 'cannot delete the root node', 'cannot delete the root node')
            return
        
        delete(self.get_item(self.tree.currentItem()))
        self.tree.currentItem().parent().removeChild(self.tree.currentItem())
        
    def show_page(self, page=None):
        if page == None:
            controller.show_page(self.get_item(self.tree.currentItem()).page)
        else:
            controller.show_page(page)
        
