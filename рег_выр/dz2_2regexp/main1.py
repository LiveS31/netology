Сергей, добрый день.
Спасибо за доработку, хорошо.
Смотрите вариант решения по моему примеру

```
from typing import Optional, List

from chardet.universaldetector import UniversalDetector
import re
import csv

Задание 1 и 2 в одном классе - читаем парсим, записываем
class ContactNormalizer:
DELIMITER = ','
ENCODING = 'utf-8'

# Наборы паттернов - можно расширять как угодно, ключи помогут не потеряться, что парсим
patterns = {
    'fio': {
        'regexp': r'^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)',
        'subst': r'\1,\3,\5,\7'
    },
    'phone': {
        'regexp': r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})',
        'subst': r'+7(\3)\4-\5-\6'},
    'add_phone': {
        'regexp': r'\(доб\.\s(\d+)\)*',
        'subst': r'доп.\1'
    }
}

def __init__(self, source_file_csv, target_file_csv='parsed_file.csv', delimiter=None, encoding=None, is_save_parsed_file=True):
    """
    Инициализация
    :param source_file_csv: пусть к файлу CSV
    :param delimiter: разделитель
    :param is_save_parsed_file: нужно ли сохранять новый файл с обработанными данными
    :param target_file_csv: путь к новому файлу
    """

    self.file = source_file_csv
    self.parsed_csv_file_path = target_file_csv
    self.is_save_parsed_file = is_save_parsed_file
    self.delimiter = delimiter or self.DELIMITER
    self.encoding = encoding or self.ENCODING
    self.parsed_data = {}

def detect_encoding(self):
    """
    Метод определения кодировки
    :return: кодировка
    """
    detector = UniversalDetector()
    with open(self.file, 'rb') as file:
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    self.encoding = detector.result['encoding']
    return self.encoding

def get_raw_data_list(self) -> Optional[List[List]]:
    """
    Метод для получения сырых данных
    :return: список списков
    """
    try:
        with open(self.file, encoding=self.detect_encoding()) as f:
            rows = csv.reader(f, delimiter=self.delimiter)
            return list(rows)
    except FileNotFoundError:
        print('Файл не найден')
        return None

def create_csv(self):
    """
    Создание нового файла
    """
    if self.parsed_data:
        with open(self.parsed_csv_file_path, "w", encoding=self.encoding) as file:
            data_writer = csv.writer(file, delimiter=self.delimiter)
            data_writer.writerows([self.parsed_data[key] for key in self.parsed_data])

def parse_data(self, row_data: List[str]) -> List[str]:
    """
    Парсинг данных и обработка согласно набору паттернов
    :param row_data: данные для парсинга - список
    :return: список с данными
    """
    row_data = ','.join(row_data)
    for key, patten in self.patterns.items():
        row_data = re.sub(patten['regexp'], patten['subst'], row_data)
    return row_data.split(',')

def check_data(self, row_data: List[str], unique_key_index: int = 0):
    """
    Проверка данных на уникальность
    :param row_data:
    :param unique_key_index: какое поле ключа используем как уникальный идентификатор
    """
    data_id = row_data[unique_key_index]

    if self.parsed_data.get(data_id):
        old_data = self.parsed_data.get(data_id)

        for index, data in enumerate(old_data):
            for new_index, new_data in enumerate(row_data):
                if new_index == index and not data and new_data:
                    old_data[index] = new_data
    else:
        self.parsed_data[data_id] = row_data

def start_parse(self):
    """
    Старт парсиннга
    :return: данные парсинга или ничего
    """
    contacts_list = self.get_raw_data_list()
    if contacts_list:
        for contact in contacts_list:
            self.check_data(self.parse_data(contact))

        if self.is_save_parsed_file:
            self.create_csv()

        return self.parsed_data

    return None
if name == 'main':
ContactNormalizer('phonebookraw.csv').startparse()

```

или вот так

```
import re
import csv
import pandas as pd

читаем адресную книгу в формате CSV в список contacts_list
with open("phonebookraw.csv", encoding="utf-8") as f:
rows = csv.reader(f, delimiter=",")
contactslist = list(rows)

TODO 1: выполните пункты 1-3 ДЗ
phonebook = []

phonebook.append(contacts_list[0])

for i in contactslist[1:]:
fio = re.findall('\w+', str(i[:3]))
lastname = fio[0]
firstname = fio[1]
if len(fio) > 2:
surname = fio[2]
else:
surname = ''
tel = re.sub('[^0-9]', '', i[5])
tel = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})(\d{4})', r'+7(\2)-\3-\4-\5 доб.\6', tel)
tel = re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})', r'+7(\2)-\3-\4-\5', tel)
newline = []
newline.extend([lastname, firstname, surname, i[3], i[4], tel, i[6]])
phonebook.append(newline)

phonebook = pd.DataFrame(phonebook)
phonebook = phonebook.rename(columns=phonebook.iloc[0])
phonebook = phonebook[1:]
phonebook = phonebook.groupby(['lastname', 'firstname']).agg(
{'surname': 'max', 'organization': 'max', 'position': 'max', 'phone': 'max', 'email': 'max'}).resetindex()
print(phonebook)
phonebook.tocsv('phonebook.csv', index=False)
```

Если нужно разобраться с кодом не забываем использовать отладку - https://yandex.ru/search/?text=pycharm+debug&clid=1955453&win=576&lr=49
