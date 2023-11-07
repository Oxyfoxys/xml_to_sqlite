from unittest import TestCase

import db_sqlite
import xml_parser


class Test(TestCase):
    def test_create_table_cd(self):
        db_sqlite.create_table_cd()

    def test_insert_data_cd(self):
        data = xml_parser.get_xml_cd('https://www.w3schools.com/xml/cd_catalog.xml')
        db_sqlite.insert_data_cd(data)

    def test_select_data_cd(self):
        db_sqlite.select_database_test()

    def test_clear_data_cd(self):
        db_sqlite.clear_table('cd')