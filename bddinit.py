#!/usr/bin/python3
# coding: utf-8

from files.models import Product, Store
from files.openfoodfacts import ProductDownloader
from files.constants import *
       
def bdd_init_main():
    downloader = ProductDownloader()
    for each_category in CATEGORY_LIST:
        products = downloader.fetch(each_category, 1000)
        for product in products:
            try:
                product = Product.create_from_openfoodfacts(**product)
            except TypeError:
                continue

if __name__ == "__main__":
    bdd_init_main()
