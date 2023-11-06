import sqlite3

con = sqlite3.connect(r'resources/food.db')

create_table_food_request = """
CREATE TABLE FOOD (
    NAME TEXT COMMENT 'Цена на товар',
    *** TEXT COMMENT '',
    *** TEXT COMMENT '',
    *** TEXT COMMENT ''
  )
"""

insert_table_food_request = """
INSERT INTO FOOD (
    NAME,
    PRODUCT_GROUP,
    FULL_NAME,
    ***
  )
values
  (?,?,?)
"""


def create_table_food():
    try:
        with con:
            con.execute(create_table_food_request)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_data_food(data):
    try:
        with con:
            con.executemany(insert_table_food_request, data)
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
            data = con.execute("SELECT * FROM USER WHERE age <= 25")
            for row in data:
                print(row)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def close_connection():
    if con:
        con.close()
        print("Соединение с SQLite закрыто")