import requests

class Cat:
    def __init__(self, num=0):
        self.catUrl = "https://cat-fact.herokuapp.com/facts"
        self.num = num

    def get(self):
        """
        this method gets the cat fact.
        args: self
        return: None
        """
        self.c = requests.get(self.catUrl)
        self.cresponse = self.c.json()[self.num]['text']
        print(self.cresponse)
    def __str__(self):
        """
        this method returns the URL and JSON dictionary format of the URL. 
        it has the args self and returns the JSON dictionary
        """
        return f'Cat({self.catUrl},{self.cresponse})'