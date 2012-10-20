from PySide.QtGui import QTextEdit
from PySide.QtGui import QListWidget
from PySide.QtGui import QTabWidget
from PySide.QtGui import QAction
from PySide.QtGui import QMessageBox
from PySide.QtCore import Qt
from controller.mainviewcontroller import rollback

class Console():
    def __init__(self, targetLayoutContainer):
        self.textarea = QTextEdit()
        self.commits = QListWidget()
        
        self.commits.addAction(QAction('Rollback to this revision', self.commits, triggered=self.rollback))
        self.commits.setContextMenuPolicy(Qt.ActionsContextMenu)
        
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
        
    def rollback(self):
        targetCommit = self.commits.currentItem().text().split(' ')[0]
        if QMessageBox.warning(None, 'Rollback to commit?', 'All commits after ' + targetCommit + ' will be lost, proceed?', QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            rollback(targetCommit)
