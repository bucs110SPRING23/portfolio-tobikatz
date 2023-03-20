import json
def main():
    news_article = "news.txt"
    news_string = open(news_article, "r").read()
    json_dict = open("subs.json")
    # json_string = json.dumps(json_dict)
    json_data = json.load(json_dict)
    for k,v in json_data.items():
        news_string = news_string.replace(k,v)

    fptr = open("betternews.txt", "w")
    fptr.write(news_string)
    fptr.close()


main ()