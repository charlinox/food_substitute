from files.models import Product, Store
from files.openfoodfacts import ProductDownloader
from files.constants import *

def main():
    downloader = ProductDownloader()
    for each_product in CATEGORY_LIST:
        products = downloader.fetch(each_product, 1000)
        for product in products:
            try:
                product = Product.create_from_openfoodfacts(**product)
            except TypeError:
                continue

    for i,choices in CATEGORY_LIST:
        print((i+1) + " : " + choices)
    choice = input ("Choisissez le numéro d'un produit à substituer ?")


if __name__ == "__main__":
    main()
