from bs4 import BeautifulSoup
import requests

def parse():
    fl = open("FIOs.txt", "w", encoding="utf8")
    firstLetter = "П"
    url = 'https://omgtu.ru/sveden/employees/'
    page = requests.get(url)
    print(page.status_code)
    if (page.status_code != 200): return
    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.find_all('td', itemprop="fio")
    for data in block:
        if (data.find('a') and data.text[0] == firstLetter):
            fl.write(data.text + "\n")
    fl.close()


if __name__ == '__main__':
    parse()