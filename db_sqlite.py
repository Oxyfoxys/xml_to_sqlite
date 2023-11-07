import sqlite3

con = sqlite3.connect(r'resources/cd.db')

create_table_cd_request = """
CREATE TABLE CD (
    TITLE TEXT COMMENT 'Название товара',
    ARTIST TEXT COMMENT 'Имя артиста',
    COUNTRY TEXT COMMENT 'Страна',
    COMPANY TEXT COMMENT 'Компания',
    PRICE TEXT COMMENT 'Цена на товар',
    YEAR TEXT COMMENT 'Год выпуска'
  )
"""

insert_table_cd_request = """
INSERT INTO CD (
    TITLE,
    ARTIST,
    COUNTRY,
    COMPANY,
    PRICE,
    YEAR
  )
values
  (?,?,?,?,?,?)
"""


def create_table_cd():
    try:
        with con:
            con.execute(create_table_cd_request)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


def insert_data_cd(data):
    try:
        with con:
            con.executemany(insert_table_cd_request, data)
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