from PySide.QtGui import QWidget
from PySide.QtGui import QDialog
from PySide.QtGui import QTextEdit
from PySide.QtGui import QTreeWidget
from PySide.QtGui import QHBoxLayout
from PySide.QtGui import QLabel
from PySide.QtGui import QTabWidget
from PySide.QtGui import QSizePolicy

class Console():
    def __init__(self, targetLayoutContainer):
        self.textarea = QTextEdit()
        targetLayoutContainer.addWidget(self.textarea)
        
    def info(self, module, function, *args):
        print module, function, args
        
        prettyString = '<font color="black"><b>', module, '</b><i>::', function, '</i> --> ', ''.join(args), '</font>'
        self.textarea.append(''.join(prettyString))
