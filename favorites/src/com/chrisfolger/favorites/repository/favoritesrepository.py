from com.chrisfolger.favorites.model.favorite import Favorite

class FavoritesRepository:
    def getFavoritesRoot(self):
        favorite = Favorite('testing')
        favorite2 = Favorite('testing again')
        favorite.children.append(favorite2)
        return favorite