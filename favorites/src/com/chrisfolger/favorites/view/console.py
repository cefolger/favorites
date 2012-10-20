from PySide.QtGui import QTextEdit
from PySide.QtGui import QListWidget
from PySide.QtGui import QTabWidget

class Console():
    def __init__(self, targetLayoutContainer):
        self.textarea = QTextEdit()
        self.commits = QListWidget()
        
        self.widget = QTabWidget()
        self.widget.addTab(self.textarea, 'Log')
        self.widget.addTab(self.commits, 'Commits')
        
        targetLayoutContainer.addWidget(self.widget)
        
    def color(self, module, function, color,  *args):
        print module, function, args
        
        prettyString = '<font color="' + color + '"><b>', module, '</b><i>::', function, '</i> --> ', ''.join(args), '</font>'
        self.textarea.append(''.join(prettyString))    
        
    def info(self, module, function, *args):
        print module, function, args
        
        prettyString = '<font color="black"><b>', module, '</b><i>::', function, '</i> --> ', ''.join(args), '</font>'
        self.textarea.append(''.join(prettyString))
        
    def error(self, module, function, *args):
        print module, function, args
        
        prettyString = '<font color="red"><b>', module, '</b><i>::', function, '</i> --> ', ''.join(args), '</font>'
        self.textarea.append(''.join(prettyString))
        
    def warn(self, module, function, *args):
        print module, function, args
        
        prettyString = '<font color="#BE9900"><b>', module, '</b><i>::', function, '</i> --> ', ''.join(args), '</font>'
        self.textarea.append(''.join(prettyString))
        
    def set_commits(self, commits):
        self.commits.clear()
        
        for commit in commits:
            self.commits.addItem(commit)
            
    def clear(self):
        self.textarea.clear()
