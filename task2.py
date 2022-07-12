import requests
from bs4 import BeautifulSoup
titlelist = {}
url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
while True:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    alllinks = soup.find("div", {"class": "mw-category mw-category-columns"})
    links = alllinks.find_all('li')
    nextlink = soup.find("a", string="Следующая страница")
    for link in links:
        link = link.find("a").get('title')
        if link[0] not in titlelist:
            titlelist[link[0]] = 0
        titlelist[link[0]] += 1

    if nextlink is not None:
        nexturl = nextlink.get('href')
        url = f"https://ru.wikipedia.org{nexturl}"

    else:
        break
for k, v in titlelist.items():
    print(f"{k}: {v}")
