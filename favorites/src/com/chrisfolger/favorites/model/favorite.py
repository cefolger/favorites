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
    
    def add_html_page(self):
        self.page = HtmlPage()
        return self.page
    
    def to_string(self):
        return self.name + ',' +  self.label + ',' + str(self.page)
    
class HtmlPage:
    def __init__(self):
        self.url = 'http://foo.com'
        self.external = True
        
    
    
            
        
