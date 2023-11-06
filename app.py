from datetime import datetime
import os
import urllib.request

def download_file(url, path, name):
    """
    Метод для загрузки файла по ссылке
    :param url: ссылка на данные
    :param path: куда сохранять
    :param name: как назвать
    :return: Ответа не возвращает
    """
    if not os.path.isdir(path):
        os.makedirs(path)
    print('Download: ' + name + ' ' + str(url) + ' >>> ' + path + os.sep + name)
    urllib.request.urlretrieve(url, path + os.sep + name)

def get_date_and_time():
    return datetime.now().strftime('_%d.%m.%Y_%H.%M.%S')