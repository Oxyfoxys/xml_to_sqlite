from unittest import TestCase

import db_sqlite
import xml_parser


class Test(TestCase):
    def test_create_table_plant(self):
        db_sqlite.create_table_plant()

    def test_insert_data_plant(self):
        data = xml_parser.get_xml_plant('https://www.w3schools.com/xml/plant_catalog.xml')
        db_sqlite.insert_data_plant(data)

    def test_select_data_plant(self):
        db_sqlite.select_database_test()

    def test_clear_data_plant(self):
        db_sqlite.clear_table('plant')