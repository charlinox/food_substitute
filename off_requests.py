#!/usr/bin/python3
# coding: utf-8

import requests
import records
import constant as constant


class BddDownload:

    def __init__(self, choice):
    self.choice = choice
    db = records.Database()
            
    def fetch_get(self, choice):
        payload = {
            'action': 'process',
            'json': '1',
            'page_size': '1000',
            'tagtype_0': 'categories',
            'tag_contains_0': 'contains',
            'tag_0': choice}
        
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?', params=payload)
        data=r.json()
        return data

    def fetch_data(self, table, fetch, limit):
        r = requests.get('https://fr.openfoodfacts.org/' + fetch + '.json')
        data=r.json()
        for f_data in data[products]:
            if f_data > limit:
                db.query("""
                INSERT INTO table VALUES(f_data)
                  """)

    def insert_data(self):
        for category in constant.category:
            off_data = fetch_get(category)
            for d in off_data:
                try:
                    data = d    
                    db.query("""
                    INSERT INTO Aliment(id, generic_name, product_name,\
                    nutriscore,url)\
                    VALUES(data)
                    """)
                except:







        