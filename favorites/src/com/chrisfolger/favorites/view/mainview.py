from PySide.QtGui import QDialog
from PySide.QtGui import QLineEdit
from PySide.QtGui import QPushButton
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QTreeWidgetItem
from pages import HtmlFavoritePage

class MainView(QDialog):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.setWindowTitle("My Form")
        
        # Create widgets
        self.edit = QTreeWidget()
        item = QTreeWidgetItem()
        item.setText(0, 'foo')
        self.edit.addTopLevelItem(item)
        self.button = QPushButton("Show Greetings")
        
        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)

    def set_favorites(self, favoritesRoot):
        self.rootId = self.treeCtrl.AddRoot(favoritesRoot.label)
        self.add_children(favoritesRoot, self.rootId)
    
    def add_children(self, node, parentId):
        for child in node.children:
            childId = self.treeCtrl.AppendItem(parentId, child.label)
            self.add_children(child, childId)
        