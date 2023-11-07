import sqlite3

con = sqlite3.connect(r'resources/plant.db')

create_table_plant_request = """
CREATE TABLE PLANT (
    COMMON TEXT COMMENT 'Группа товара',
    BOTANICAL TEXT COMMENT 'Название на товар',
    ZONE TEXT COMMENT 'Расположение  товара',
    LIGHT TEXT COMMENT 'Свет товара',
    PRICE TEXT COMMENT 'Цена на товар',
    AVAILABILITY TEXT COMMENT 'Артикул товара'
  )
"""

insert_table_plant_request = """
INSERT INTO PLANT (
    COMMON,
    BOTANICAL,
    ZONE,
    LIGHT,
    PRICE,
    AVAILABILITY
  )
values
  (?,?,?,?,?,?)
"""


def create_table_plant():
    try:
        with con:
            con.execute(create_table_plant_request)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_data_plant(data):
    try:
        with con:
            con.executemany(insert_table_plant_request, data)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def clear_table(table_name):
    try:
        with con:
            con.execute('DELETE FROM ' + table_name)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def drop_table(table_name):
    try:
        with con:
            con.execute('DROP TABLE IF EXISTS ' + table_name)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def select_database_test():
    try:
        with con:
            data = con.execute("SELECT * FROM PLANT")
            for row in data:
                print(row)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def close_connection():
    if con:
        con.close()
        print("Соединение с SQLite закрыто")