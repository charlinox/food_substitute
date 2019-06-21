@dataclass
class Product:
    '''Class of Products.'''
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
    Product: str


@dataclass
class Favorite:
    '''Class for favorites.'''
    name: str
    Product_as_original: str
    Product_as_substitut: str


@dataclass
class Category:
    '''Class for categorie.'''
    name: str
    product: str
