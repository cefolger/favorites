from repository.favoritesrepo import FavoritesRepository

model = None
repository = None 
logger = None


def start(mainviewModel):
    global model
    global repository
    global logger 
     
    model = mainviewModel
    logger = model.get_logger()
    print 'hello'
    
    repository = FavoritesRepository(logger)
    model.set_favorites(repository.get_favorites_root())
