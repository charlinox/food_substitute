#! /usr/bin/env python3
# coding: utf-8

import records

class BddManager
    """
    This class manage the relation to OFF BDD
    """

    def __init__(self):
        """
        Initialize the connection to the BDD.
        """

        db = records.Database()

    def create_table(self):
        """Creation of tables."""

        db.query("""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                generic_name VARCHAR(140) NOT NULL,
                product_name  VARCHAR(140) NOT NULL,
                brands  VARCHAR(100),
                nutriscore char NOT NULL,
                url varchar(255)  
                PRIMARY KEY (id)
            )""")

        db.query("""
            CREATE TABLE IF NOT EXISTS Category (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                category VARCHAR(140) NOT NULL,
                PRIMARY KEY (id)
            )""")

        db.query("""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                store VARCHAR(140) NOT NULL,
                PRIMARY KEY (id)
            )""")

        db.query("""
            CREATE TABLE IF NOT EXISTS Favorite (
                id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                substitut int unsigned references Aliment(id),
                original int unsigned references Aliment(id),
                PRIMARY KEY (id)
            )""")

        db.query("""
            CREATE TABLE IF NOT EXISTS Asso_product_category (
                aliment int unsigned,
                category int unsigned,
                CONSTRAINT pfk_aliment
                    FOREIGN KEY (aliment)
                    REFERENCES Aliment(id),
                CONSTRAINT pfk_category
                    FOREIGN KEY (category)
                    REFERENCES Category(id),
                PRIMARY KEY (aliment, category)
            )""")

        db.query("""
            CREATE TABLE IF NOT EXISTS Asso_product_store (
                aliment int unsigned,
                store int unsigned,
                CONSTRAINT pfk_aliment
                    FOREIGN KEY (aliment)
                    REFERENCES Aliment(id),
                CONSTRAINT pfk_store
                    FOREIGN KEY (store)
                    REFERENCES Store(id),
                PRIMARY KEY (aliment, store)
            )""")

    def 