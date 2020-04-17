from bs4 import BeautifulSoup
import requests
import pandas as pd


soup = BeautifulSoup(open("C:/Users/azfar/Desktop/exambazaar scraping/exambazaar_eng.html", "rb"))

container = soup.find_all("a", {"id":"reviewLink", "class":"ng-binding", "target":"_blank",
                               "ui-sref":"x5({ nameslug:coachingGroup.nameslugs[0], areaslug:coachingGroup.areaslugs[0], exam:examId })"})

data = {"Name": [],
        "url": []}

for i in range(len(container)):
    data["Name"].append(container[i].text)
    data["url"].append(container[i].get("href"))

data = pd.DataFrame(data)
data = data.drop_duplicates(subset = "url")
print(data.head())
data.to_csv("eng_links.csv")
