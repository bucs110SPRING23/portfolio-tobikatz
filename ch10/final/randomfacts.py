import requests


class Randomfacts:
    def __init__(self):
        self.Url = "https://api.adviceslip.com/advice"
    def get(self):
        """
        this method gets random advice from the random advice api. 
        args: self
        return: none
        """
        self.fact = requests.get(self.Url)
        self.response = self.fact.json()['slip']['advice']
        print(self.response)
    def __str__(self):
        """
        this method returns the internal string unchanged. 
        it has the args self and returns the JSON dictionary
        """
        return self.reponse






