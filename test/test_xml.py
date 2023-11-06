from unittest import TestCase

import app
import xml_parser


class Test(TestCase):
    def test_download_xml_plant(self):
        app.download_file('https://www.w3schools.com/xml/plant_catalog.xml', 'resources',
                          'plant_catalog_xml' + app.get_date_and_time() + '.xml')

    def test_parse_xml_plant(self):
        data = xml_parser.get_xml_plant('https://www.w3schools.com/xml/plant_catalog.xml')
        for i in data:
            print(i)
