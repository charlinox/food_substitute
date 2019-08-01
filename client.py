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
            main_choice = input("  Sélectionnez votre choix en indiquant son numéro : ")
            if main_choice in ("1", "2", "3"):
                return main_choice
        
    def category_loop(self):
        """ Category menu """
        while True:
            print("\n")
            for i, category in enumerate(CATEGORY_LIST):
                print(f"  {i+1} - {category}")
            category_choice = input("\n  Sélectionnez la catégorie en entrant son numéro parmis les choix suivants : ")
            if category_choice.isdigit():
                category_choice = int(category_choice)
                if 0 < category_choice <= len(CATEGORY_LIST):
                    return CATEGORY_LIST[category_choice-1]

    def product_loop(self, category_choice):
        """ Product menu """
        while True:
            category = Category.objects.get(name=category_choice)
            list_product = []
            print("\n")
            for i, product in enumerate(Product.all_products):
                list_product.append(product)
                if i < 10:
                    print(f"  {i+1} - {product.name}")
                else:
                    break
            product_choice = input("\n  Sélectionnez l'aliment en entrant son numéro parmis les choix suivants : ")
            if product_choice.isdigit():
                product_choice = int(product_choice)
                if 0 < product_choice <= 10:
                    return list_product[product_choice-1]

    def substitutes_loop(self, product_choice):
        """ Menu displaying the three best substitutes """
        # product_choice = Product.objects.get(name=product_choice.name)
        print (f"product_choice as product : {product_choice}") # Test
        while True:
            best_substitutes = Product.objects.fine_substitutes(product_choice)
            print (f"best_substitutes : {best_substitutes}") # Test
            list_substitutes = []
            print("\n")
            for i, substitute in enumerate(best_substitutes):
                if i < 10:
                    print(f"  {i+1} - {substitute.name} - indice nutritionnel : {substitute.nutrition_grade.upper()}")
                    list_substitutes.append(substitute)
                else:
                    break
            substitute_choice = input("\n  Sélectionnez un substitut en entrant son numéro parmis les choix suivants : ")
            if substitute_choice.isdigit():
                substitute_choice = int(substitute_choice)
                if 0 < substitute_choice <= 10:
                    return list_substitutes[substitute_choice-1]


    def substitut_display(self, substitute_choice, product_choice):
        """ Menu displaying the details of the chosen substitute """
        print (f"substitute_choice : {substitute_choice}, product_choice : {product_choice}") # Test
        while True:
            print(
                "\n  Voici les détails du substitut que vous avez sélectionné :\n"
                f"  Nom du produit : {substitute_choice.name}\n"
                "  Au moins un magasin ou l'acheter :\n"
            )
            stores = Store.objects.get_some_by_product(substitute_choice, 3)
            print (f"stores : {stores}")
            for store in stores:
                print(f"   {store.name}\n")
            print(
                f"  Score nutritionnel : {substitute_choice.nutrition_grade.upper()}\n"
                f"  Adresse web du produit : {substitute_choice.url}\n"
            )
            save_choice = input("\n  Souhaitez vous enregistrer le résultat dans la base de données (O/N) ? : ").upper()
            if save_choice == "O":
                Favorite.objects.save(product_choice, substitute_choice)
                self.start()
            elif save_choice == "N":
                self.start()

    def favorite_display(self):
        """  Menu displaying the details of the original and substitued products  """
        favorites = Favorite.objects.get_all_favorite()
        for i, favorite in enumerate(favorites):
            print(
                "\n  Le produit original     ==>  {favorites.original}\n"
                "    Le produit substitué ==>  {favorites.substitute}\n"
                "    url                     : {favorites.url}\n"
                "    nutrition_grade         : {favorites.nutrition_grade}\n"
                "    Magasins                : {favorites.stores}\n"
                )
            if i % 4 == 0 and i != 0:
                print("\n  Souhaitez vous afficher les substitutes suivants (O/N) ?")
                again_choice = input("\n").upper()
                if again_choice == "O":
                    continue
                elif again_choice == "N":
                    self.start()
        self.start()


    def start(self):
        """  Main frame  """
        print(
            "\n  Bienvenue dans cette application qui va vous permettre de "
            "  manger mieux grace à Open Food Facts !\n"
            "  Que souhaitez vous faire ?\n"
            )
        main_choice = self.main_loop()
        if main_choice == "1":
            category_choice = self.category_loop()
            product_choice = self.product_loop(category_choice)
            substitute_choice = self.substitutes_loop(product_choice)
            favorite = self.substitut_display(substitute_choice, product_choice)
        if main_choice == "2":
            self.favorite_display()
        if main_choice == "3":
            print("  Au revoir !")


        


            
