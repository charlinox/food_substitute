#! /usr/bin/env python3
# coding: utf-8

from files.models import Product, Store, Category, Favorite
from files.constants import *


class Client:
    """ Main frame """

    def main_loop(self):
        """ Main menu """
        while True:
            print(
                "  1 - Substituer un aliment\n"
                "  2 - Retrouver mes aliments substitués\n"
                "  3 - Sortir du programme\n"
            )
            main_choice = input("\n")
            if main_choice in ("1", "2", "3"):
                return main_choice
        
    def category_loop(self):
        """ Category menu """
        while True:
            print("\n  Sélectionnez la catégorie en entrant son numéro parmis les choix suivants :")
            for i, category in enumerate(CATEGORY_LIST):
                print(f"  {i+1} - {category}")
            category_choice = input()
            if category_choice.isdigit():
                category_choice = int(category_choice)
                if 0 < category_choice <= len(CATEGORY_LIST):
                    return CATEGORY_LIST[category_choice-1]
        return category_choice

    def product_loop(self, category_choice):
        """ Product menu """
        while True:
            print("  Sélectionnez l'aliment en entrant son numéro parmis les choix suivants :")
            categories = Category.objects.get(name=category_choice)
            list_product = []
            for i, product in enumerate(categories.products):
                list_product.append(product)
                if i < 10:
                    print(f"  {i+1} - {product.name}")
                else:
                    break
            product_choice = input()
            if product_choice.isdigit():
                product_choice = int(product_choice)
                if 0 < product_choice <= 10:
                    return list_product[i-1]

    def substituts_loop(self, product_choice):
        """ Menu displaying the three best substitutes """
        while True:
            print("  Sélectionnez un substitut en entrant son numéro parmis les choix suivants :")
            best_substituts = Product.objects.fine_substituts(product_choice)
            list_substituts = []
            for i, substitute in enumerate(best_substituts.substitute):
                if i < 10:
                    print(f"  {i+1} - {substitute}")
                    list_substituts[i] = append(substitute)
                else:
                    break
            substitut_choice = input("\n")
            if substitut_choice.isdigit():
                substitut_choice = int(substitut_choice)
                if 0 < substitut_choice <= 3:
                    return list_substituts[i-1]


    def substitut_display(self, substitut_choice, product_choice):
        """ Menu displaying the details of the chosen substitute """
        while stay:
            print(
                "Voici les détails du substitut que vous avez sélectionné :\n"
                "Nom du produit : {substitut_choice.product.name}\n"
                "Au moins un magasin ou l'acheter :\n"
            )
            stores = Stores.objects.get_some_by_product(substitut_choice, 3)
            for store in stores:
                print(f"   {store.name}\n")
            print(
                "Score nutritionnel : {substitut_choice.product.nutrition_grade}\n"
                "Adresse web du produit : {substitut_choice.product.url}\n\n"
                "Souhaitez vous enregistrer le résultat dans la base de données (O/N) ?"
            )
            save_choice = input("\n").upper()
            if save_choice == "O":
                Favorite.objects.save(product_choice, substitut_choice)
                self.start()
            elif save_choice == "N":
                self.start()

    def favorite_display(self):
        """  Menu displaying the details of the original and substitued products  """
        favorites = Favorite.objects.get_all_favorite()
        for i, favorite in enumerate(favorites):
            print(
                "Le produit original     ==>  {favorites.original}\n"
                "   Le produit substitué ==>  {favorites.substitute}\n"
                "   url                     : {favorites.url}\n"
                "   nutrition_grade         : {favorites.nutrition_grade}\n"
                "   Magasins                : {favorites.stores}\n\n"
                )
            if i % 4 == 0 and i != 0:
                print("Souhaitez vous afficher les substituts suivants (O/N) ?")
                again_choice = input("\n").upper()
                if again_choice == "O":
                    continue
                elif again_choice == "N":
                    self.start()
        self.start()


    def start(self):
        """  Main frame  """
        main_choice = self.main_loop()
        if main_choice == "1":
            category_choice = self.category_loop()
            product_choice = self.product_loop(category_choice)
            substitut_choice = self.substituts_loop(product_choice)
            favorite = self.substitut_display(substitut_choice, product_choice)
        if main_choice == "2":
            self.favorite_display()
        if main_choice == "3":
            pass

        


            
