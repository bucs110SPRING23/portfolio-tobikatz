import requests


class Randomfacts:
    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"
    def get(self):
        """
        this method gets random advice from the random advice api. 
        args: self
        return: none
        """
        self.fact = requests.get(self.url)
        self.response = self.fact.json()['slip']['advice']
        print(self.response)
    def __str__(self):
        """
        this method returns the url and the advice string. 
        it has the args self and returns the JSON dictionary
        """
        return f'Randomfacts({self.url},{self.response})'






