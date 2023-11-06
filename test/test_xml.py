from unittest import TestCase

import app
import xml_parser


class Test(TestCase):
    def test_download_xml_florcom(self):
        app.download_file('https://www.w3schools.com/xml/simple.xml', 'resources',
                          'simple_xml' + app.get_date_and_time() + '.xml')

    def test_parse_xml_food(self):
        xml_parser.get_xml_food('https://www.w3schools.com/xml/simple.xml')