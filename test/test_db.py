from unittest import TestCase

import db_sqlite
import xml_parser


class Test(TestCase):
    def test_create_table_food(self):
        db_sqlite.create_table_food()

    def test_insert_data_food(self):
        data = xml_parser.get_xml_food('https://www.w3schools.com/xml/simple.xml')
        db_sqlite.insert_data_food(data)

    def test_select_data_food(self):
        db_sqlite.select_database_test()

    def test_clear_data_food(self):
        db_sqlite.clear_table('food')