import requests
def main():
    response = requests.get("https://wizard-world-api.herokuapp.com/swagger/index.html/Wizards")
    print(response.headers)
    print(response.json())

main()
