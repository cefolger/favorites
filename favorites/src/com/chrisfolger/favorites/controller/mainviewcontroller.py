from com.chrisfolger.favorites.repository.favoritesrepository import FavoritesRepository

model = None
repository = FavoritesRepository()

def start(mainviewModel):
    global model
    model = mainviewModel
    print 'hello'
    model.set_favorites(repository.get_favorites_root())