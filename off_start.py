#!/usr/bin/python3
# coding: utf-8

import off_bdd.py as OffBdd
import off_requests as OffReq 


class Off:
    """ class integrating the initialization and the main frames of the app """

    def __init__(self):
        OffBdd.BddManager()
        OffReq.create_table()

    def start():


