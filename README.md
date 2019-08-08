# food_substitute
Projet 5 OpenClassrooms

This repository contains the source code that I use for my N°5 project presentation.

You want to change your diet but do not know where to start. Replace Nutella with hazelnut paste, yes, but which one? And in which store to buy it? This solution is a program that interacts with the Open Food Facts database to retrieve food, compare it to offer you a healthier substitute for the one you want.

# Features:

The user is on the terminal that shows him the following choices:

1 - Quel aliment souhaitez-vous remplacer ?

2 - Retrouver mes aliments substitués

3 - Sortir du programme

The user selects 1. The program asks the user the following questions and the user selects the answers:

Select the category by entering its number from the following choices: [Several proposals associated with a number. The user enters the corresponding digit and press [enter].

Select the food. [Several proposals associated with a number. The user enters the digit corresponding to the chosen food and presses enter]

The program offers a substitute, its description, a store where he can buy it (if any) and a link to the Open Food Facts page about that food.

The user can then save the result in the database and then come back to the main menu.

# Requirements :

To install and run this app, you need:

Python 3.7+

git (only to clone this repository)

# Installation :

The commands below set everything up to run the examples :

$ git clone https://github.com/charlinox/food_substitute.git

$ cd food_substitute-master

$ pip3 install pipenv ou $ pip install pipenv

$ pipenv install

First initialize the local database :

$ pipenv run bddinit.py

Then launch the app :

$ pipenv run off.py
