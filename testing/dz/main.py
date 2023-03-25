import requests
#изменение домашнего задания под функцию

#Задание 1
def city(geo_logs):
    geo_logg =[]
    for i in range (len(geo_logs)):
        if geo_logs[i]['visit'+str(i+1)][1] =='Россия':
        #print (geo_logs[i]['visit'+str(i+1)][0])
            geo_logg.append((geo_logs[i]['visit'+str(i+1)][0]))

    return geo_logg

geo_log = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

#задача 2
def summ(id):
    b =[]
    for i in range (len (id)):
        for j in (id['user'+(str(i+1))]):
            b.append(j)
    # print ([*set(b)])
    #или
    #print([*set(sum(id.values(),[]))])
    return [*set(b)]

ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
#задание 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

#Задание 5
def yandex(listss):

    dic = listss[-1] # или dic = lists.pop()
    for i in (listss[-2::-1]): # или for i in reversed(lists):
       dic = {i:dic}
    #print (dic)
    return dic





lists = ['2018-01-01', 'yandex', 'cpc', 100]
if __name__ == '__main__':
    city(geo_log)
    summ(ids)
    #social(stats)
    yandex(lists)

