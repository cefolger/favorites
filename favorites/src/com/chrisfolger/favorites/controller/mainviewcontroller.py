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
    repository.new_repo(directory)
    # load the favorites from it
    favorites = repository.get_favorites_root(directory)
    model.set_favorites(favorites)