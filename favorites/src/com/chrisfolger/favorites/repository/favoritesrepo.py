from model.favorite import Favorite
import git

class FavoritesRepository:
    def __init__(self, logger):
        self.dirty = False   
        self.logger = logger     
    
    def get_favorites_root(self, path):
        self.logger.info(__name__, ' get_favorites_root',' grabbing all favorites from ', path)
        
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
        
    def new_repo(self, directory):
        # create the repository 
        return git.init_repo(directory)
        
    def add_favorite(self, directory,  title):
        self.logger.info(__name__, 'add_favorite', directory, title)
        git.cd(directory)
        git.status()
        
