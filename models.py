@dataclass
class Aliment:
    '''Class of aliment.'''
    name: None
    nutriscore: str
    brand: str
    url: str
    originals: str
    substitutes: str
    stores: str
    categories: str


@dataclass
class Store:
    '''Class for stores.'''
    name: str
    aliments: str


@dataclass
class Favorite:
    '''Class for favorites.'''
    name: str
    aliment_as_original: str
    aliment_as_substitut: str


@dataclass
class Categorie:
    '''Class for categorie.'''
    name: str
    aliments: str
