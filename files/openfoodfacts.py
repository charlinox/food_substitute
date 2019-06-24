import requests


class ProductDownloader:

    def fetch(self, categories, number=20):
        payload = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": categories,
            "page_size": number,
            "json": 1,
        }

        response = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl", params=payload)
        data = response.json()
        return data['products']
