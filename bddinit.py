#!/usr/bin/python3
# coding: utf-8

from files.models import Product, Store
from files.openfoodfacts import ProductDownloader
from files.constants import *
       
def bdd_init():
    downloader = ProductDownloader()
    for each_category in CATEGORY_LIST:
        products = downloader.fetch(each_category, 100)
        for product in products:
            try:
                product = Product.create_from_openfoodfacts(**product)
            except TypeError:
                continue