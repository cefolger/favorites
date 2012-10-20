from com.chrisfolger.favorites.model.favorite import Favorite

class FavoritesRepository:
    def __init__(self):
        self.dirty = False        
    
    def get_favorites_root(self):
        favorite = Favorite('testing')
        favorite2 = Favorite('testing again')
        favorite.children.append(favorite2)
        self._favorites = favorite
        return favorite
    
    def save_favorite(self, favorite):
        self.dirty = True
        
    def flush(self):
        # flush to the git repository 
        self.dirty = False 
        
