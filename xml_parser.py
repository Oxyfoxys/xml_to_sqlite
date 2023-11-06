import urllib.request as urllib2

import xmltodict


def get_xml_food(url):
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    products = data.get('breakfast_menu')
    print('breakfast_menu')
    print(str(len(products['food'])))
    for position in products['food']:
        print('')
        print('name: ', position['name'])
        print('price: ', position['price'])
        print('description: ', position['description'])
        print('calories: ', position['calories'])