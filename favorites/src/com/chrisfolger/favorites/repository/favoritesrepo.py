from model.favorite import Favorite
import git
import os

class FavoritesRepository:
    def __init__(self, logger):
        self.logger = logger     
    
    def get_favorite_from_directory(self, directory):
        titleFile = open(directory + '/title', 'r')
        title = titleFile.readline()
        titleFile.close()
        
        favorite = Favorite(title)
        return favorite
    
    def get_favorites_root(self, directory):
        favoritesDirectory = directory + '/favorites'
        self.logger.info(__name__, ' get_favorites_root',' grabbing all favorites from ', directory + '/favorites')
        rootFavoriteEntry = [name for name in os.listdir(directory + '/favorites') if os.path.isdir(os.path.join(directory + '/favorites', name))][0]
        
        favorite = self.get_favorite_from_directory(favoritesDirectory + '/' + rootFavoriteEntry)
       
        for child in [name for name in os.listdir(favoritesDirectory + '/' + rootFavoriteEntry) if os.path.isdir(os.path.join(favoritesDirectory + '/' + rootFavoriteEntry, name))]:
            favorite.children.append(self.get_favorites_children(os.path.join(favoritesDirectory + '/' + rootFavoriteEntry, child)))
       
        return favorite
    
    def get_favorites_children(self, currentNodeDirectory):
        self.logger.info(__name__, 'get_favorites_children', currentNodeDirectory)
        
        favorite = self.get_favorite_from_directory(currentNodeDirectory)
        
        for child in [name for name in os.listdir(currentNodeDirectory) if os.path.isdir(os.path.join(currentNodeDirectory, name))]:
            favorite.children.append(self.get_favorites_children(os.path.join(currentNodeDirectory, child)))
        
        return favorite
    
    def new_repo(self, directory):
        # create the repository 
        return git.init_repo(directory)
        
    def save_favorite(self, directory, name, title=None):
        self.logger.info(__name__, 'save_favorite', directory, name, title)
        if not title == None:
            git.cd(directory + '/favorites/' + name)
            favorite = open('title', 'w+')
            favorite.write(title)
            favorite.close()
            git.add()
            output, errors = git.commit("updated " + name + " with new title '" + title + "'")
            if not errors == "":
                self.logger.error(__name__, 'save_favorite', directory, title, errors)
                return False
            return True
        
    def add_favorite(self, directory,  name, title):
        self.logger.info(__name__, 'add_favorite', directory, title)
        git.cd(directory)
        git.makedir(directory + '/favorites/' + name)
        favorite = open(directory + '/favorites/' + name + '/title', 'w+')
        favorite.write(title)
        favorite.close()
        git.add()
        git.commit('added new favorite ' + name + ' with title ' + title)
        
