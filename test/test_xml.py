from unittest import TestCase

import app


class Test(TestCase):
    def test_download_xml_florcom(self):
        app.download_file('https://www.w3schools.com/xml/simple.xml', 'resources',
                          'simple_xml' + app.get_date_and_time() + '.xml')