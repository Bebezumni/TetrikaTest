import requests

session = requests.Session()
letters = {}
api_url = "https://ru.wikipedia.org/w/api.php"
api_params = {
    "action": "query",
    "format": "json",
    "list": "categorymembers",
    "cmtitle": "Категория:Животные_по_алфавиту",
    "cmlimit": 500,
}
while True:
    request = session.get(url=api_url, params=api_params)
    data = request.json()
    for entry in data['query']['categorymembers']:
        letter = entry['title'][0].upper()
        if (letter in letters):
            letters[letter] += 1
        else:
            letters[letter] = 1
    if ('continue' in data):
        api_params['cmcontinue'] = data['continue']['cmcontinue']
    else:
        break
print(letters)