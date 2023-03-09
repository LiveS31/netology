from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#print(contacts_list) #info

name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
a = list()
for card in contacts_list:
    card_as_string = ','.join(card)
    formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
    card_as_list = formatted_card.split(',')
    a.append(card_as_list)
#pprint(a) #info

# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
name_list = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_rec = r'\1\3\10\4\6\9\7\8'
num_list = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб.)*(.)(\s*)(\d+)*(\)*)'
num_rec = r'+7(\4)\8-\11-\14\15\17\18\20'

tabl_new = list() #создание списка
for i in contacts_list[:-1]: #сразу убираем пустой элемент
    temp = ','.join(i) #разделяем запятыми
    temp = re.sub(name_list, name_rec, temp) #убираем лишние запятые
    temp = re.sub(num_list, num_rec, temp) # наводим порядок в номерах
    table_list = temp.split(',') #делим по символу
    tabl_new.append(table_list) #добавляем через цикл
#print(tabl_new) #ИНФО


for i in tabl_new: # запускаем цикл по списку
    for j in tabl_new: # запускаем проверку списка по списку
        if i[0] == j[0] and i[1] == j[1] and i is not j:
            if i[2] == '': # при условии, что позиция 2 = пустоте приравниваем к тому же списку
                             # по которому пробегаем циклом
                i[2] = j[2] # приравниваем у нас получаются полностью дубликаты в таблице
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
contacts_list = list() # создаем цикл для заполнения
for page in tabl_new: # делаем проход цикла, чтобы пройтись по нему
    if page not in contacts_list: # создаем условие - если строки нет в списке - добавляем
                                     # тем самым избавляемся от дубликатов
        contacts_list.append(page) # добавляем по условию выше

# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
