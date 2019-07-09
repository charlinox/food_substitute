#! /usr/bin/env python3
# coding: utf-8

from files.models import Product, Store, Category, Favorite
from bddinit import bdd_init
from files.constants import *


class Client:
    """ Main frame """

    def main_loop(self):
        """ Main menu """

        start_menu = 0
        while True:
            print(
                "1 - Quel aliment souhaitez-vous remplacer ?\n"
                "2 - Retrouver mes aliments substitués.\n"
                "3 - Sortir du programme.\n"
            )
            main_choice = inputs()
            if main_choice in ("1", "2", "3"):
                return main_choice
        

    def category_loop(self):
        """ Category menu """
        while True:
            print("Sélectionnez la catégorie en entrant son numéro parmis les choix suivants :")
            for i, category in enumerate(CATEGORY_LIST)
                print(f"{i+1} - {category}"
            category_choice = input()
            if category_choice.isdigit():
                category_choice = int(category_choice)
                if 0 < category_choice <= len(CATEGORY_LIST):
                    return CATEGORY_LIST[category_choice-1]

        return category_choice

    def product_loop(self, category_choice):
        """ Product menu """
        while True:
            print("Sélectionnez l'aliment en entrant son numéro parmis les choix suivants :")
            category = Category.objects.get(name=category_choice)
            list_product = []
            for i, product in enumerate(category.products)
                list_product[i] = append(product)
                if i < 10:
                    print(f"{i+1} - {product}"
                else:
                    break
            product_choice= = input()
            if product_choice.isdigit():
                product_choice = int(product_choice)
                if 0 < product_choice <= 10:
                    return list_product[i-1]

    def substituts_loop(self, product_choice):
        """ Menu displaying the three best substituts """
            print("Sélectionnez un substitut en entrant son numéro parmis les choix suivants :")
        best_substituts = Product.objects.fine_substituts(name=product_choice)
        list_substituts = []
        for i, substitut in enumerate(best_substituts.products)
            list_substituts[i] = append(substitut)
                print(f"{i+1} - {substitut}"
        print(
                f"Voici les trois meilleurs substituts à ce produit : {}\n"
                "Les magasins ou l'acheter :\n"
                for store in Stores.objects.get
                "3 - Sortir du programme.\n"
            )

        #   name
        #   stores
        #   url

        print("Souhaitez vous enregistrer le résultat dans la base de données (O/N) ?")
        save_choice = inputs().upper()
        while stay:
            if save_choice == "O":
                # Enregistrer en bdd le produit original et son substitut
                stay = False
            elif save_choice == "N":
                stay = False

        

    def start():
        """  Main frame  """
        main_choice = self.main_loop()
        if main_choice == "1":
            category_choice = self.category_loop()
            product_choice = self.product_loop(category_choice)
            self.substituts_loop(product_choice)
        if main_choice == "2":

            
