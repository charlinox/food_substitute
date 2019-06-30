#! /usr/bin/env python3
# coding: utf-8

from files.models import Product, Store, Category, Favorite
from bddinit import bdd_init
from files.constants import *


class Client:
    """ class integrating the initialization and the main frames of the app """

    def __init__(self):

    def main_loop(self):
        """ Main screen  """
        stay = True
        start_menu = 1
        while stay:
            print("""
                1 - Quel aliment souhaitez-vous remplacer ?"/n
                2 - Retrouver mes aliments substitués./n
                3 - Sortir du programme.
                """)
            main_choice = int(inputs())
            while stay:
                if main_choice == 1:
                    print("Sélectionnez la catégorie en entrant son numéro parmis les choix suivants :")
                    print(f"{((category).index)+1)} :{category}" for category in CATEGORY_LIST)) # start_menu possible
                    category_choice = CATEGORY_LIST[inputs()-1]
                    while stay:
                        print("Sélectionnez l'aliment en entrant son numéro parmis les choix suivants :")
                        category = Category.products(category_choice)
                        print(f"{(lambda start_menu: start_menu += 1)} :{product}" for product in category.products))
                        
                        # Possibilité de faire comme ca aussi :
                        # category = Category.products(category_choice)
                        # for product in category.products:
                        #     print(f"{(lambda start_menu: start_menu += 1)} :{product}")

                        product_choice = int(inputs())
                        while stay:                   
                            # Rechercher dans la bdd le premier produit appartenant à la même
                            # catégorie et ayant le nutriscore le plus faible
                            # puis l'afficher ainsi :
                            #   name
                            #   brand
                            #   stores
                            #   url  

                            print("Souhaitez vous enregistrer le résultat dans la base de données (O/N) ?")
                            save_choice = inputs().upper()
                            while stay:
                                if save_choice == "O":
                                    # Enregistrer en bdd le produit original et son substitut
                                elif save_choice == "N":
                                    # Revenir au menu principal

                if main_choice == 2:
                    

                if main_choice == 3:
                    stay = False
        

    def start():
        """  Main frame  """
        bdd_init()
        self.main_loop()