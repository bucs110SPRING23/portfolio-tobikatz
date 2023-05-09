import requests

class Dog:
    def __init__(self):
        self.dogUrl = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/?number=1"
    def lyrics(self):
        self.dogFact = requests.get(self.dogUrl)
        