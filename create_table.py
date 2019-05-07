CREATE DATABASE OPEN_FOOD_FACTS_FR CHARACTER SET 'utf8mb4';
CREATE TABLE IF NOT EXISTS Aliment (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    generic_name VARCHAR(140) NOT NULL,
    product_name  VARCHAR(140) NOT NULL,
    brands  VARCHAR(100) NOT NULL,
    ingredients_text TEXT,  
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS Categorie (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    categories VARCHAR(140) NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS Store (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    stores VARCHAR(140) NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE IF NOT EXISTS Asso_aliment_categorie (
    CONSTRAINT pfk_aliment_categorie
        FOREIGN KEY (aliment)
        REFERENCES Aliment(id)
    CONSTRAINT pfk_categorie
        FOREIGN KEY (categorie)
        REFERENCES Aliment(id)
)

ENGINE=INNODB;