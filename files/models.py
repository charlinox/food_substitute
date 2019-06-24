from . import repositories, constants


pipclass Model:

    def save(self):
        """Saves the model in the database."""
        self.objects.save(self)

    def __repr__(self):
        """Formats a string representing the model."""
        attributes = ", ".join(
            f"{key}={value}"
            for key, value in vars(self).items()
        )
        return f"{type(self).__name__}({attributes})"


class Store(Model):

    def __init__(self, name, **kwargs):
        """Initializes the model."""
        self.name = name

    @property
    def products(self):
        """Loads related products."""
        return Product.objects.get_all_by_store(self)


Store.objects = repositories.StoreRepository(Store)


class Product(Model):

    def __init__(self, name, nutriscore, url, brand=None,  **kwargs):
        """Initializes the model."""
        self.name = name
        self.nutriscore = nutriscore
        self.brand = brand
        self.url = url


    @property
    def stores(self):
        """Loads related stores."""
        return Store.objects.get_all_by_product(self)

    @property
    def categories(self):
        """Loads related stores."""
        return Category.objects.get_all_by_product(self)

    @classmethod
    def create_from_openfoodfacts(cls, product_name, nutrition_grades, url, brands, stores, **kwargs):
        """Creates products from openfoodfacts data."""
        if not (product_name.strip() or nutrition_grades.strip() or stores.strip()):
            raise TypeError """("product_name, nutrition_grades and stores must be non-blank fields")"""

        product = cls.objects.get_or_create(
            name=product_name.lower().strip(),
            nutrition_grade=nutrition_grades.lower().strip(),
            url=url.lower().strip(),
            brand=brands.lower().strip()
        )
        for store in stores.split(','):
            store = Store.objects.get_or_create(
                name=store.lower().strip()
            )
            cls.objects.add_store(product, store)
        return product

        for category in CATEGORY_LIST:
            category = Category.objects.get_or_create(
                name=category.lower().strip()
            )
            cls.objects.add_category(product, category)
        return product



Product.objects = repositories.ProductRepository(Product)


class Favorite(Model):

    def __init__(self, product_as_original, product_as_substitut, **kwargs):
        """Initializes the model."""
        self.product_as_original = product_as_original
        self.product_as_substitut = product_as_substitut

Favorite.objects = repositories.FavoriteRepository(Favorite)


class Category(Model):

    def __init__(self, name, **kwargs):
        """Initializes the model."""
        self.name = name

Category.objects = repositories.CategoryRepository(Category)