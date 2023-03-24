
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
    #print ([*set(b)])
    #или
    print([*set(sum(id.values(),[]))])
    return

ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
#задание 3


def seach(sech):
    for j in range (1,len(sech)+1):
        word1 = 0
        for i in sech:
            if len(i.split()) == (j):
                word1 += 1
        if word1 != 0:
            if j ==1:
                print(f'Поисковых запросов из {j}-ого словa: {(round(word1/(len(sech))*100))}')
            else:
                print (f'Поисковых запросов из {j}-х слов: {(round(word1/(len(sech))*100))}')
    return


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
#задание 4
def social(soc):

    for key,donat in soc.items():
        if donat == max(stats.values()):
            print (key)
    return

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


#Задание 5
def yandex(list):

    dic = list[-1] # или dic = lists.pop()
    for i in (list[-2::-1]): # или for i in reversed(lists):
       dic = {i:dic}
    print (dic)
    return

def geo_logs_list(geo_list):
    geo_logs_filter = []
    for visit in geo_list:
        for countries in visit.values():
            if 'Россия' in countries:
                geo_logs_filter.append(visit)
    return geo_logs_filter


lists = ['2018-01-01', 'yandex', 'cpc', 100]
if __name__ == '__main__':
    city(geo_log111s)
    # summ(ids)
    # seach(queries)
    # social(stats)
    # yandex(lists)

