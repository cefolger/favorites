class Favorite:
    def __init__(self, label, name = ''):
        self.label = label 
        self.name = name
        self.children = []
        self.tags = []
        self.parent = None
    
    def getFullPath(self):
        currentNode = self.parent
        path = self.name
        
        while(currentNode != None):
            path = currentNode.name + '/' + path
            currentNode = currentNode.parent
        
        return path
            
        
class HtmlFavorite(Favorite):
    def __init__(self):
        self.link = ''
        
class TextFavorite(Favorite):
    def __init__(self):
        self.text = ''
        