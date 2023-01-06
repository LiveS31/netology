
# Работа с pandos
#import display as display
import pandas as pd
#import displayfunction as display
# читаем данные из cvs, который находится в zip- файле на github
#pands умеет открыать файлы даже в архиве и выводить на экран
url = 'https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html'# адрес
df = pd.read_csv(url, encoding='ISO-8859-1')#,compression='zip') #путь/ кодировка/ сжатие
#Далее выводим первые 5 строк ( df.head() ), и последние 5 строк ( df.tail() )
#Это выводится для понимания, что все ок
print (df.head())
print (df.tail())
#расчитать базовую статистику
df.describe()
# оставляем данные только с положительным результатом
        # В [   ] =- столбцы из файла
df = df[(df['UniPracce']>0)& (df['Quantity']>0 )]
# 'UniPracce' и 'Quantity' - являются столбцами. взять все значения больше 0
df.describe()
#чтоб сохранить например в xl эту талицу:
df.to_excel('11.xlsx')
#чтоб сохранить например в csv эту талицу:
df.to_csv('11.csv')
#Посмотреть сколько дублей в таблице:
print (df.duplicated().sum()) # посмотреть сколько дублей и ссумировать их
#Удалить дубли в таблице
df = df.drop_duplicates()
print (df.shape)
#Сколько строк всего
print (df.shape) # shape -проверка количества данных
# посмотреть тип объекта в файле
df.info()
# так объекты могут быть только одно типа - их нужно этому привести если они отличаются
#datatype
df['CustometID'] = df['CustometID'].astype('Int64')
# перевод даты из строкового формата в datetime
df['InvoceData'] = pd.to_datetime(df['InvoiceDate'])
#считаем сколько транзакций было по страницам при поможи value_conts
df['Country'].value_counts()
#подсчет количества уникальных клиентов
countries = df.goupby['Country']['CustomerID'].nunique().sort_values(assendin=False)
#добавим месяц покупки в новый стобец при помощи df.strftime('%y - %m')
df ['InvoiceMonth'] = df['InvoiceMounth'].df.strtime('%y - %m')
df['InvoiceMounth']
#считание уникальное количество клиентов в динамике по месецам
df.groupby['InvoceMounth']['CustomerID'].nunique()# .plot ()  -график , (kind=bai) - другой график
#фиксируем день недели
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek+1
#посчитем количество клиентов для дня недели
df.groupby['DayOfweek']['InvoiceNo'].nuniqur()
#Создадим новы столбец
df['Revenue'] = df['Quantity']*df['UniPrice']
df.head()
#Выручка за месяц
df.groupby('InvoiceMonth')['Revenue'].sum()



