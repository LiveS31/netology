#преобразование в словарь
cook_book = {}
with open('recipes.txt') as f: #чтение из файла
    for line in f:
        name_food = line.strip()
        count_ing = int(f.readline())
        ing_food = list()
        for i in range (count_ing):
            ings = {}
            ingr = f.readline().strip()
            ings['ingredient_name'], ings['quantity'], ings['measure'] = ingr.split('|')
            ings['quantity'] = int(ings['quantity'])
            ing_food.append(ings)
        f.readline()
        cook_book[name_food] = ing_food

# with open('menu.txt','w') as a: #запись в фаил
#     a.write (str(cook_book))
# print(cook_book)

#функция выбора блюд
def get_shop_list_by_dishes(dishes, person_count): # создаем функцию
    ingred = {} # создаем словарь
    for duch in dishes: # дербаним значения ввода на ключи
        if duch in cook_book: # пробегаем ключами по словарю
            for menu_duch in cook_book[duch]: # подставляем ключи в словарь- получем значения по ключей
                ing = {} # создаем словарь + и обнуление
                ing['measure'] = menu_duch['measure'] # заполняем словарь ing
                ing['quantity'] = menu_duch['quantity']*person_count # заполняем словарь ing
                ingred[menu_duch['ingredient_name']] = ing # добовляем вновый словарь ing
        else:
            ingred = 'нет такого блюда'
    print (ingred)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#get_shop_list_by_dishes(input('введите введите блюдо на выбор:'),int(input('введите колличество персон:')))


# пеборка файлов
def file_txt(txt1, txt2, txt3):
    cont1 =0 #создаем счетчик 1
    dict_file ={}

    with open (txt1, 'r') as f1:      #считаем кол-во строк в файле 1
        for line1 in f1:
            cont1+=1
        dict_file[cont1] = txt1

    cont2=0   #создаем счетчик 2
    with open (txt2, 'r') as f2:   #считаем кол-во строк в файле 2
        for line2 in f2:
            cont2+=1
    dict_file[cont2] =txt2

    cont3= 0   #создаем счетчик  3
    with open (txt3, 'r') as f3:  #считаем кол-во строк в файле 3
        for line3 in f3:
            cont3+=1
    dict_file[cont3] = txt3
    #определяем мин, ср, макс строк
    min_list= min(cont3, cont2, cont1)
    sr_list = ((cont3+cont2+cont1)-((max(cont3,cont2,cont1)+min(cont3,cont2,cont1))))
    max_list= max(cont3, cont2, cont1)
    part = [min_list,sr_list,max_list]    #создаем массив для цикла записи
    # создаем цикл для записи с учем сортировки
    for v in part:
        with open(dict_file[v], 'r') as f:
            with open('total.txt','a') as rec:
                rec.write(f'Имя файла: {dict_file[v]}\n')
                rec.write(f'Количество строк в файле: {v}\n')
            for lines in f:
                with open('total.txt', 'a', encoding='utf-8') as rec:
                    rec.write(lines)
    print ('Внесение изменения в файл: total.txt')
file_txt('1.txt', '2.txt', '3.txt')

#решение задачи 3 от преподователя