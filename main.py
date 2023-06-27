import requests
from bs4 import BeautifulSoup as bs
n = 1
list_u = []
file = open('hotgames_url_list.txt', 'w', encoding='UTF-8')
while n != 3:
    r = requests.get('https://hot-game.info/'+f'{n}')
    src = r.text
    soup = bs(src, 'lxml')
    find = soup.find_all(class_='game-title')
    for i in find:
        list_u.append(i.text)
        print(i.text)
        file.write(i.text)
    n +=1