class Favorite:
    def __init__(self, label, name = ''):
        self.label = label 
        self.name = name
        self.children = []
        self.tags = []
        self.parent = None
        self.page = None
    
    def getFullPath(self):
        currentNode = self.parent
        path = self.name
        
        while(currentNode != None):
            path = currentNode.name + '/' + path
            currentNode = currentNode.parent
        
        return path
    
    def add_html_page(self, url = 'http://foo.com'):
        if self.page != None:
            return self.page
        
        self.page = HtmlPage(self.label, self, url)
        return self.page
    
    def to_string(self):
        return self.name + ',' +  self.label + ',' + str(self.page)
    
    def get_page(self):
        return self.page
    
class HtmlPage:
    def __init__(self, label, item, url = 'http://foo.com'):
        self.url = url
        self.external = True
        self.label = label
        self.item = item
    def serialize(self):
        return self.url
    def description(self):
        return self.url
    def get_type(self):
        return 'html'
        
    
    
            
        
