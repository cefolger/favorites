class Favorite:
    def __init__(self, label):
        self.label = label 
        self.children = []
        self.tags = []
        
class HtmlFavorite(Favorite):
    def __init__(self):
        self.link = ''
        
class TextFavorite(Favorite):
    def __init__(self):
        self.text = ''
        