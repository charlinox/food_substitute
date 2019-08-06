#!/usr/bin/python3
# coding: utf-8

from .database import db
from .exceptions import NotFoundError, NotUniqueError


class Repository:

    def __init__(self, model):
        """Initializes the repository."""
        self.db = db
        self.model = model
        self.create_table()

    @property
    def last_id(self):
        """Returns the last auto-incremented id."""
        rows = self.db.query("""
            SELECT LAST_INSERT_ID() AS id
        """)
        for row in rows:
            return row['id']

    def filter(self, **search_terms):
        """Searches objects in the database matching the provided criteria."""
        conditions = " AND ".join(
            [f"{term} = :{term}"
            for term, value in search_terms.items()
            if value is not None]
        ).strip()

        if conditions:
            conditions = f"WHERE {conditions}"

        instances = self.db.query(f"""
            SELECT * from {self.table}
            {conditions}
        """, **search_terms).all(as_dict=True)

        return [
            self.model(**instance)
            for instance in instances
        ]

    def get(self, **search_terms):
        """Gets one object from the database matching the provided criteria."""
        instances = self.filter(**search_terms)

        if not instances:
            raise NotFoundError("Nothing has been found.")

        if len(instances) > 1:
            raise NotUniqueError("Serveral instance have been found.")

        return instances[0]

    def get_or_create(self, **search_terms):
        """Gets one object from the database matching the provided criteria or
        creates it if it does not exist.
        """
        try:
            instance = self.get(**search_terms)
        except NotFoundError:
            instance = self.create(**search_terms)
        return instance

    def all(self):
        """Returns all the objects of the current type in the database."""
        return self.filter()

    def create(self, **attributes):
        """Create a new instance of the model and saves it in the database."""
        return self.save(self.model(**attributes))

    def create_table(self):
        """Creates the necessary tables for the current model to work."""
        pass

    def save(self, instance):
        """Saves or updates the current model instance in the database."""
        return instance


class StoreRepository(Repository):

    table = 'store'

    def create_table(self):
        """Creates the store table on local bdd.""" 
        self.db.query(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                name VARCHAR(140) NOT NULL,
                PRIMARY KEY (id)
            )
        """)

    def save(self, store):
        """Saves the store on local bdd.""" 
        self.db.query(f"""
            INSERT INTO {self.table} (id, name)
            VALUES (:id, :name)
            ON DUPLICATE KEY UPDATE  name = :name
        """, **vars(store))

        if not store.id:
            store.id = self.get(name=store.name).id
        return store

    def add_product(self, store, product):
        """Adds product on product_store on local bdd."""
        self.db.query("""
            INSERT IGNORE INTO product_store(product_id, store_id)
            VALUES (:product_id, :store_id)
        """, product_id=product.id, store_id=store.id)

    def get_some_by_product(self, product, how_many):
        """Gets some stores for a product on local bdd."""
        stores = self.db.query(f"""
            SELECT store.id, store.name from store
            JOIN product_store ON product_store.store_id = store.id
            JOIN product ON product_store.product_id = product.id
            WHERE product.id = :id
            LIMIT :how_many
        """, id=product.id, how_many=how_many).all(as_dict=True)
        return [self.model(**store) for store in stores]


class ProductRepository(Repository):

    table = 'product'

    def create_table(self):
        """Creates the product  and product_store tables on local bdd."""
        self.db.query(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id BIGINT UNSIGNED NOT NULL,
                name VARCHAR(140) NOT NULL,
                nutrition_grade char NOT NULL,
                url varchar(255),
                PRIMARY KEY (id)
            )
        """)

        self.db.query("""
            CREATE TABLE IF NOT EXISTS product_store (
                product_id bigint unsigned,
                store_id int unsigned,
                CONSTRAINT pfk_product
                    FOREIGN KEY  (product_id)
                    REFERENCES product(id),
                CONSTRAINT pfk_store
                    FOREIGN KEY (store_id)
                    REFERENCES store(id),
                PRIMARY KEY (product_id, store_id)
            )
        """)

    def save(self, product):
        """Saves the product on local bdd."""
        self.db.query(f"""
            INSERT INTO {self.table} (id, name, nutrition_grade, url)
            VALUES (:id, :name, :nutrition_grade, :url)
        """, **vars(product))
        return product

    def add_store(self, product, store):
        """Adds a store on product_store."""
        self.db.query("""
            INSERT IGNORE INTO product_store(product_id, store_id)
            VALUES (:product_id, :store_id)
        """, product_id=product.id, store_id=store.id)

    def get_favorite_by_product(self, product):
        """Adds a store on product_store."""
        products = self.db.query(f"""
            SELECT product.id, product.name from store
            JOIN product_store ON product_store.store_id = store.id
            JOIN product ON product_store.product_id = product.id
            WHERE store.id = :id
        """, id=product.id).all(as_dict=True)
        return [self.model(**product) for product in products]

    def add_category(self, product, category):
        """Adds a category on product_category."""
        self.db.query("""
            INSERT IGNORE INTO product_category(product_id, category_id)
            VALUES (:product_id, :category_id)
        """, product_id=product.id, category_id=category.id)

    def fine_substitutes(self, product_choice):
        """Finds better substitutes to the one provided."""
        substitutes = self.db.query("""
        SELECT  product.id, product.name, product.nutrition_grade, product.url, count(*) FROM product 
        JOIN product_category ON product.id = product_category.product_id
        WHERE 
            product.id != :product_choice_id

            AND product_category.category_id IN (
                SELECT category_id FROM product_category
                WHERE product_id = :product_choice_id
            )

            AND product.nutrition_grade < (
                SELECT nutrition_grade FROM product
                WHERE product.id = :product_choice_id
            )

        -- On groupe par nom de produit pour l'aggrégation
        GROUP BY product.id

        -- On ordonne par nombre décroissant de tags communs
        ORDER BY count(*) DESC, MAX(:product_choice_nutrition_grade) ASC
        """, product_choice_id=product_choice.id, product_choice_nutrition_grade=product_choice.nutrition_grade)
        return [self.model(**substitute) for substitute in substitutes]

    def get_all_by_category(self, category):
        """Gets all the products for a given category."""
        products = self.db.query(f"""
            SELECT product.id, product.name, product.nutrition_grade, product.url from product
            JOIN product_category ON product_category.product_id = product.id
            JOIN category ON product_category.category_id = category.id
            WHERE category.id = :id
        """, id=category.id).all(as_dict=True)
        return [self.model(**product) for product in products]

class CategoryRepository(Repository):

    table = 'category'

    def create_table(self):
        """Creates the category and product_category tables."""
        self.db.query(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                name VARCHAR(140) NOT NULL,
                PRIMARY KEY (id)
            )
        """)

        self.db.query("""
            CREATE TABLE IF NOT EXISTS product_category (
                product_id bigint unsigned,
                category_id int unsigned,
                CONSTRAINT pfk_product_2
                    FOREIGN KEY (product_id)
                    REFERENCES product(id),
                CONSTRAINT pfk_category_2
                    FOREIGN KEY (category_id)
                    REFERENCES category(id),
                PRIMARY KEY (product_id, category_id)
            )
        """)

    def save(self, category):
        """Saves the category into bdd."""
        self.db.query(f"""
            INSERT INTO {self.table} (id, name)
            VALUES (:id, :name)
            ON DUPLICATE KEY UPDATE  name = :name
        """, **vars(category))
        return category

    def get_all_by_category(self, category):
        """Gets all the products for a given category."""
        products = self.db.query(f"""
            SELECT product.id, product.name, product.nutrition_grade from product
            JOIN product_category ON product_category.product_id = product.id
            JOIN category ON product_category.category_id = category.id
            WHERE category.id = :id
        """, id=category.id).all(as_dict=True)
        return [self.model(**product) for product in products]


class FavoriteRepository(Repository):

    table = 'favorite'

    def create_table(self):
        """Creates the favorite table."""
        self.db.query(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                substitut_id bigint unsigned references product(id),
                original_id bigint unsigned references product(id),
                PRIMARY KEY (substitut_id, original_id)
            )
        """)

    def save(self, substitute_choice, product_choice):
        """Creates the favorite table."""
        self.db.query(f"""
            INSERT INTO {self.table} (substitut_id, original_id)
            VALUES (:substitut_id, :original_id)
        """, substitut_id=substitute_choice.id, original_id=product_choice.id)
        favorite = (substitute_choice.id, product_choice.id)
        return favorite

    def get_all_favorite(self):
        """Get all the favorites."""
        products = self.db.query(f"""
            SELECT original.`name` as "product_as_original", substitute.`name` as "product_as_substitut", substitute.`url` as "url", \
            substitute.`nutrition_grade`, GROUP_CONCAT(DISTINCT store.`name` SEPARATOR ', ') \
            as stores FROM favorite as fav
            JOIN product as original ON original.id = fav.original_id
            JOIN product as substitute ON substitute.id = fav.substitut_id
            JOIN product_store ON product_store.product_id = substitute.id
            JOIN store ON store.id = product_store.store_id
            GROUP BY original.name, substitute.name, substitute.url, substitute.nutrition_grade
        """).all(as_dict=True) # Un moyen de trier les stores en fonction du nombre de produits par store dans la base off ? 
        return [self.model(**product) for product in products]
