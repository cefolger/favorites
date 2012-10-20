from model.favorite import Favorite
import git
import os

class FavoritesRepository:
    def __init__(self, logger):
        self.logger = logger     
    
    def get_favorite_from_directory(self, directory, name):
        titleFile = open(directory + '/title', 'r')
        title = titleFile.readline()
        titleFile.close()
        
        favorite = Favorite(title, name)
        return favorite
    
    def get_favorites_root(self, directory):
        favoritesDirectory = directory + '/favorites'
        self.logger.info(__name__, ' get_favorites_root',' grabbing all favorites from ', directory + '/favorites')
        rootFavoriteEntry = [name for name in os.listdir(directory + '/favorites') if os.path.isdir(os.path.join(directory + '/favorites', name))][0]
        
        favorite = self.get_favorite_from_directory(favoritesDirectory + '/' + rootFavoriteEntry, rootFavoriteEntry)
       
        for child in [name for name in os.listdir(favoritesDirectory + '/' + rootFavoriteEntry) if os.path.isdir(os.path.join(favoritesDirectory + '/' + rootFavoriteEntry, name))]:
            childFavorite = self.get_favorites_children(os.path.join(favoritesDirectory + '/' + rootFavoriteEntry, child), child)
            childFavorite.parent = favorite
            favorite.children.append(childFavorite)
       
        return favorite
    
    def get_favorites_children(self, currentNodeDirectory, name):
        self.logger.info(__name__, 'get_favorites_children', currentNodeDirectory)
        
        favorite = self.get_favorite_from_directory(currentNodeDirectory, name)
        
        for child in [name for name in os.listdir(currentNodeDirectory) if os.path.isdir(os.path.join(currentNodeDirectory, name))]:
            childFavorite = self.get_favorites_children(os.path.join(currentNodeDirectory, child), child)
            childFavorite.parent = favorite 
            favorite.children.append(childFavorite)
        
        return favorite
    
    def new_repo(self, directory):
        # create the repository 
        return git.init_repo(directory)
        
    def save_favorite(self, directory, name, title=None, page = None):
        self.logger.info(__name__, 'save_favorite', directory, name)
        
        if not title == None:
            git.cd(directory + '/favorites/' + name)
            favorite = open('title', 'w+')
            favorite.write(title)
            favorite.close()
            git.add()
            output, errors = git.commit("updated " + name + " with new title " + title)
            if not errors == "":
                self.logger.error(__name__, 'save_favorite', directory, title, errors)
                return False
            return True
        elif not page == None:
            git.cd(directory + '/favorites/' + name)
            favorite = open('page', 'w+')
            favorite.write(page.serialize())
            favorite.close()
            git.add()
            output, errors = git.commit("updated " + name + " with new page " + page.description())
            if not errors == "":
                self.logger.error(__name__, 'save_favorite', directory, page, errors)
                return False
            return True
        
    def sync(self, directory):
        self.logger.info(__name__, 'sync', directory)
        git.cd(directory)
        if git.changesExist():
            self.logger.warn(__name__, 'sync', 'changes detected, syncing')
            git.add(' -u')
            git.add()
            git.commit('committing repository state before loading favorites')
            return True
        self.logger.info(__name__, 'sync', 'no changes detected')
        return False
            
        
    def add_favorite(self, directory,  name, title, existing=''):
        self.logger.info(__name__, 'add_favorite', directory, title)
        git.cd(directory)
        git.makedir(directory + '/favorites/' + existing + name)
        favorite = open(directory + '/favorites/' + existing + name + '/title', 'w+')
        favorite.write(title)
        favorite.close()
        git.add()
        git.commit('added new favorite ' + name + ' with title ' + title)
        
    def get_commits(self, directory):
        self.logger.info(__name__, 'get_commits', directory)
        git.cd(directory)
        return git.get_commits().split('\n')
    
    def rollback(self, directory, commit = None):
        if commit == None:
            git.cd(directory)
            git.rollback()
