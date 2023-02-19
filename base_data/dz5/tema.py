import psycopg2

with psycopg2.connect(database="", user="", password="") as conn:
    with conn.cursor() as cur:
        def new_table(cura):
            cura.execute("""
                DROP TABLE numbers;
                DROP TABLE name_surname_email;

                CREATE TABLE IF NOT EXISTS name_surname_email(
                id SERIAL PRIMARY KEY not null,
                name VARCHAR,
                surname VARCHAR,
                email VARCHAR
                );

                CREATE TABLE IF NOT EXISTS numbers(
                id SERIAL  PRIMARY KEY not null,
                id_name INTEGER  REFERENCES name_surname_email(id),
                number VARCHAR
                );
                """)


        conn.commit()  # фиксируем в БД

        def new_client(id,  nam, surn, em, phon): # добавление нового клиента
            cur.execute("""
            INSERT INTO name_surname_email(name, surname, email) VALUES(%s, %s, %s);
            """ ,(nam, surn, em))
            cur.execute("""
            INSERT INTO numbers(id_name, number) VALUES(%s, %s)
            """, (id, phon))

        def add_nub(id, num):
            cur.execute("""
            INSERT INTO numbers(id_name, number) VALUES(%s, %s);
            """, (id, num))

        def change_data(id, nam, surn, em): # Изменение данных о клиенте
            cur.execute("""
            UPDATE name_surname_email SET name = %s, surname =%s, email = %s WHERE id =%s;
            """, ( nam, surn, em, id))

        def change_phone(id, phon): #изменения номера телефона
            cur.execute("""
            UPDATE numbers SET number = %s WHERE id = %s;
            """, ( phon, id))
        def del_client(id):
            cur.execute("""
            DELETE FROM numbers WHERE id_name = %s;
            """,(id,))
            cur.execute("""
            DELETE FROM name_surname_email WHERE id = %s;
            """,(id,))
        def search(searcht):
            cur.execute("""
            SELECT * FROM name_surname_email WHERE surname = %s;
            """, (searcht,))
            print(cur.fetchone())
            cur.execute("""
            SELECT * FROM name_surname_email WHERE name = %s;
            """, (searcht,))
            print(cur.fetchone())
            cur.execute("""
            SELECT * FROM name_surname_email WHERE email = %s;
            """, (searcht,))
            print(cur.fetchone())
            cur.execute("""
            SELECT * FROM numbers WHERE number = %s;
               """, (searcht,))
            print(cur.fetchone())





# запуск функциий
        #new_table(cur) # создание таблиц
        #new_client( 1,'lef', 'LLef', 'dsfsdf', 'fdhdfb') #заполнение таблиц
        #add_nub(2,'34234') # Добавление номера существующего клиента
        #change_data(1, 'gd1fg', 'susd111f1rn', 'ems2d12f') #изменение даннх клиента
        #change_phone(1,'djn ') # изменение номера телефона
        #del_client(1) #Функция, позволяющая удалить существующего клиента
        search('dsfsdf')



#conn.commit()
#table(cur)
#def new_user(name): #, curn, emai,phone):
# print(name)



# while  True:
#     print('Выберите действия:\n'
#         '1 - создание таблиц\n'
#         '2 - добавление нового клиента\n'
#                   '3 - добавление номера телефона для нового клиента\n'
#                   '4 - изменение данных нового клиента\n'
#                   '5 - удаление телефона существующего клиента\n'
#                   '6 - удалить клиента\n'
#                   '7 - найти нового клиента')
#     answ = input()
#     if answ == '1':
#         print("Таблица создана")
#         new_table(cur)
#    #  elif answ == '2':
#      print ('hbdsgkdsgvk')
#      table('12')
# # answ = ''
conn.close()
