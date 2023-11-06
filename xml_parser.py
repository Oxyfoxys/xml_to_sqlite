import urllib.request as urllib2

import xmltodict


def get_xml_plant(url):
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    products = data.get('CATALOG')
    # print('breakfast_menu')
    # print(str(len(products['food'])))
    my_array = []
    for position in products['PLANT']:
        my_list = [position['COMMON'], position['BOTANICAL'], position['ZONE'], position['LIGHT'], position['PRICE'], position['AVAILABILITY']]
        my_array.append(my_list)

        # print('')
        # print('name: ', position['name'])
        # print('price: ', position['price'])
        # print('description: ', position['description'])
        # print('calories: ', position['calories'])
    # print(my_array)

    # for i in my_array:
    #     print(i)
    return my_array