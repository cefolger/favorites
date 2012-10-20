from repository.favoritesrepo import FavoritesRepository
from repository.git import init_repo
from repository.git import set_logger

model = None
repository = None 
logger = None

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
    # load the favorites from it
    favorites = repository.get_favorites_root(directory)
    model.set_favorites(favorites)
    
def open_repository(directory):
    favorites = repository.get_favorites_root(directory)
    model.set_favorites(favorites)