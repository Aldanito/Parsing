import requests
from bs4 import BeautifulSoup
import csv
import time
import json
import requests

URL = 'https://shop.kz/smartfony/filter/almaty-is-v_nalichii-or-ojidaem-or-dostavim/apply/?PAGEN_1='
HEADERS = {'User-Agent': 'Mozilla/5.0'}
HOST = 'https://shop.kz'
FILE = '../../../smartphones.json'
count = 1

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='bx_catalog_item')
    catalog = []
    for item in items:
        # print(item)
        item = item.div['data-product']
        item = json.loads(item)
        if item['name'].find('GB') != -1:
            gb = 'GB,'
            mem = (item['name'][item['name'].index(',')+2:item['name'].index(gb)+2])
            gb = 'GB'
        else:
            gb = 'Gb,'
            mem = (item['name'][item['name'].index(',') + 2:item['name'].index(gb)+2])
            gb = 'Gb'
        mem = mem.replace(gb, ' Гб')
        catalog.append({
            'name': item['name'][item['name'].index(' ')+1:],
            'articul': item['id'],
            'price': item['price'],
            'memory-size': mem.replace(gb, ' Гб'),
        })
    return catalog


def save_file(items, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent = 6,ensure_ascii=False)
    file.close()
def parse():
    """ URL = input('Введите URL: ')
    URL = URL.strip() """
    count = 0
    list = []
    catalog = []
    for i in range(1,2):
        list.append(URL + str(i))
    for i in list:
        count += 1
        print(f'Парсинг страницы {count} {len(list)+1}...')
        html = get_html(i)
        catalog.extend(get_content(html.text))
        time.sleep(1)
    ctl = {}
    ctl.update({'id':catalog})
    save_file(ctl, FILE)
parse()