#Задание 1

geo_logs = [
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
for i in range (len(geo_logs)):
  if geo_logs[i]['visit'+str(i+1)][1] =='Россия':
        print (geo_logs[i]['visit'+str(i+1)][0])


#задача 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
b =[]
for i in range (len (ids)):
    for j in (ids['user'+(str(i+1))]):
        b.append(j)
print ([*set(b)])
#или
print([*set(sum(ids.values(),[]))])


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

for j in range (1,len(queries)+1):
    word1 = 0
    for i in queries:
        if len(i.split()) == (j):
            word1 += 1
    if word1 != 0:
        if j ==1:
            print(f'Поисковых запросов из {j}-ого словa: {(round(word1/(len(queries))*100))}')
        else:
            print (f'Поисковых запросов из {j}-х слов: {(round(word1/(len(queries))*100))}')



#задание 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
for key,donat in stats.items():
    if donat == max(stats.values()):
        print (key)


#Задание 5

lists = ['2018-01-01', 'yandex', 'cpc', 100]
dic = lists[-1] # или dic = lists.pop()
for i in (lists[-2::-1]): # или for i in reversed(lists):
   dic = {i:dic}
print (dic)



