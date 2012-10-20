class Favorite:
    def __init__(self, label, name = ''):
        self.label = label 
        self.name = name
        self.children = []
        self.tags = []
        
class HtmlFavorite(Favorite):
    def __init__(self):
        self.link = ''
        
class TextFavorite(Favorite):
    def __init__(self):
        self.text = ''
        