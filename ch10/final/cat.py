import requests

class Cat:
    def __init__(self):
        self.catUrl = "https://cat-fact.herokuapp.com"
    def lyrics(self):
        self.catFact = requests.get(self.catUrl)
        