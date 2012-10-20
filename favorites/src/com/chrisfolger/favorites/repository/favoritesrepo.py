from model.favorite import Favorite

class FavoritesRepository:
    def __init__(self):
        self.dirty = False        
    
    def get_favorites_root(self):
        favorite = Favorite('testing')
        favorite2 = Favorite('testing again dddd')
        favorite3 = Favorite('testing still again')
        favorite.children.append(favorite2)
        favorite2.children.append(favorite3)
        self._favorites = favorite
        return favorite
    
    def save_favorite(self, favorite):
        self.dirty = True
        
    def flush(self):
        # flush to the git repository 
        self.dirty = False 
        
