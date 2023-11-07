from unittest import TestCase

import app
import xml_parser


class Test(TestCase):
    def test_download_xml_cd(self):
        app.download_file('https://www.w3schools.com/xml/cd_catalog.xml', 'resources',
                          'cd_catalog_xml' + app.get_date_and_time() + '.xml')

    def test_parse_xml_cd(self):
        data = xml_parser.get_xml_plant('https://www.w3schools.com/xml/cd_catalog.xml')
        for i in data:
            print(i)
