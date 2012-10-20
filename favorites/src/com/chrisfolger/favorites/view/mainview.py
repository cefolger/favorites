from pages import HtmlFavoritePage
from PySide.QtGui import QDialog

class MainView(QDialog):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.setWindowTitle("My Form")

    def set_favorites(self, favoritesRoot):
        self.rootId = self.treeCtrl.AddRoot(favoritesRoot.label)
        self.add_children(favoritesRoot, self.rootId)
    
    def add_children(self, node, parentId):
        for child in node.children:
            childId = self.treeCtrl.AppendItem(parentId, child.label)
            self.add_children(child, childId)
        