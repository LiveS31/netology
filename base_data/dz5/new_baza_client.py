import psycopg2

with psycopg2.connect(database="", user="", password="") as conn:
    with conn.cursor() as cur:

        cur.execute ("""

        --DROP TABLE numbers;
        --DROP TABLE name_surname_email;

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
# creat_tabels(cur.execute)
# # # conn.close()
# # # with conn.cursor() as cur:
# #         cur.execute ("""
# #         insert into name_surname_email values( 1,'hkh', 'iuguyk', 'hkjhggy');
# #         INSERT INTO numbers values(1 ,1, 'nkjhk');
#
#     # """)
#     conn.commit()
# #     with conn.cursor() as cur:
# #          cur.execute("""
# #           SELECT id FROM name_surname_email WHERE id=%s where name =%s;
# #           """, (1 , 'name',))  # хорошо, обратите внимание на кортеж
# #          print(cur.fetchone())
# #conn.commit()
# conn.close()
# answ=[]
# #while answ != 'q':
# print('Выберите действия:\n'
#     '1 - создание таблиц\n'
#     '2 - добавление нового клиента\n'
#           '3 - добавление номера телефона для нового клиента\n'
#           '4 - изменение данных нового клиента\n'
#           '5 - удаление телефона существующего клиента\n'
#           '6 - удалить клиента\n'
#           '7 - найти нового клиента')
# answ = input()
# # if answ == 'e':
# #     break
# if answ == '1':
#     creat_tabels(cur.execute)
#
#
# def news_client(name, surname, email, phone):
#     name = n
#     surname = sn
#     number = nu
#     print(n, sn, nu)
#
#
# news_client(input('name:'), input('surname:'),
#             input('email:'), int(input('number:')))