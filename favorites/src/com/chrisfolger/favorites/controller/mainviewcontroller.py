from repository.favoritesrepo import FavoritesRepository
from repository.git import init_repo
from repository.git import set_logger
import random
from model.favorite import Favorite

model = None
repository = None 
logger = None
repositoryDirectory = ''

def start(mainviewModel):
    global model
    global repository
    global logger 
     
    model = mainviewModel
    logger = model.get_logger()
    set_logger(logger)
    
    repository = FavoritesRepository(logger)

def new_repository(directory):
    # create the repository 
    result = repository.new_repo(directory)
    if(not result):
        logger.error(__name__, 'new_repository', 'repository was not created, stopping')
        return
    # add an example favorite 
    repository.add_favorite(directory, 'example', 'the title of the example')
    repository.save_favorite(directory, 'example', 'a new title')
    open_repository(directory)
    
def open_repository(directory):
    global repositoryDirectory
    repositoryDirectory = directory
    
    favorites = repository.get_favorites_root(directory)
    repository.sync(directory)
    #commit any changes on load 
    model.set_favorites(favorites)
    
def add_child(node):
    name = str(random.randrange(100000))
    title = 'atitle'
    
    repository.add_favorite(repositoryDirectory, name, title,  node.getFullPath() + '/')

    favorite = Favorite(title, name)
    favorite.parent = node     
    return favorite

def save(node, newTitle=''):
    if not newTitle == '':
        repository.save_favorite(repositoryDirectory, node.getFullPath(), newTitle)
