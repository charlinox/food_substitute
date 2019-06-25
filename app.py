from files.models import Product, Store
from files.openfoodfacts import ProductDownloader
from files.constants import *

def main():
    downloader = ProductDownloader()
    for each_category in CATEGORY_LIST:
        products = downloader.fetch(each_category, 1000)
        for product in products:
            try:
                product = Product.create_from_openfoodfacts(**product)
            except TypeError:
                continue

    # for i,choice in :
    #     print((i+1) + " : " + choice)
    # choice = input("Choisissez le numéro d'un produit à substituer ?")


if __name__ == "__main__":
    main()
