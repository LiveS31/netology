import psycopg2



def new_table():
    cur.execute("""
                
                CREATE TABLE IF NOT EXISTS name_surname_email(
                id_client SERIAL PRIMARY KEY,
                name VARCHAR,
                surname VARCHAR,
                email VARCHAR
                );

                CREATE TABLE IF NOT EXISTS numbers(
                id_phones SERIAL  PRIMARY KEY,
                id_name INTEGER  REFERENCES name_surname_email(id_client),
                number INTEGER
                );
                """)
    print('Таблица создана!!!')

    conn.commit()  # фиксируем в БД

#удаление таблиц
def del_table():
    cur.execute("""
    DROP TABLE numbers;
    DROP TABLE name_surname_email;
    """)
def new_client(nam=None, surn=None, em=None, phon=None): # добавление нового клиента
    cur.execute("""
            INSERT INTO name_surname_email(name, surname, email) VALUES(%s, %s, %s)
            RETURNING id_client, name, surname;
            """ ,(nam, surn, em))
    id_client = cur.fetchone()
    if phon is not None:
        cur.execute("""
            INSERT INTO numbers(id_name, number)
            VALUES(%s, %s) RETURNING number;
            """, (id_client[0], phon))
        cur.fetchone()
    print('Клиент', *id_client[1:], 'добавлен(-а) в таблицу.')

#добовление номера
def add_nub(id_client, num):
    cur.execute("""
            INSERT INTO numbers(id_name, number)
            VALUES(%s, %s)
            RETURNING id_name, numbers;
            """, (id_client, num))
    number = cur.fetchone()
    print(f'Изменение номера клиента {number[0]} - выполнено')

# Изменение данных о клиенте
def change_data(id, nam=None, surn=None, em=None, phon=None): # Изменение данных о клиенте
    if nam is not None:
        cur.execute("""
        UPDATE name_surname_email SET name=%s WHERE id_client=%s;
        """, (nam, id))
    if surn is not None:
        cur.execute("""
        UPDATE name_surname_email SET surname=%s WHERE id_client=%s;
        """,(surn, id))
    if em is not None:
        cur.execute("""
        UPDATE name_surname_email SET email=%s WHERE id_client=%s;
        """, (em, id))
    if phon is not None:
        cur.execute("""
        UPDATE numbers SET number=%s WHERE id_name=%s;
        """,(phon, id))
    print(f'Данные клиента с id {id} изменены.')

 #изменения номера телефона
def change_phone(id, phon): #изменения номера телефона
    cur.execute("""
            UPDATE numbers SET number = %s WHERE id_name = %s;
            """, ( phon, id))
    print(f'Данные телефона клиента с id {id} изменены.')

#Удалениея номера телефона клиента
def del_pnones(id, phon):
    cur.execute("""
    DELETE FROM numbers WHERE id_name=%s AND number=%s;
    """, (id, phon))


#удаление клиента
def del_client(id):
    cur.execute("""
            DELETE FROM numbers WHERE id_name = %s;
            """,(id,))
    cur.execute("""
            DELETE FROM name_surname_email WHERE id_client = %s;
            """,(id,))
    print(f'Клиент id {id} - удален')

#поиск клиента
def search(searcht):
    cur.execute("""
            SELECT * FROM name_surname_email AS nse
            LEFT JOIN numbers AS n ON nse.id_client = n.id_name
            WHERE nse.name LIKE %s;
            """, (searcht,))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0],cur.fetchone()[1],cur.fetchone()[2],cur.fetchone()[3],cur.fetchone()[6])
        return
    cur.execute("""
            SELECT * FROM name_surname_email AS nse
            LEFT JOIN numbers AS n ON nse.id_client = n.id_name
            WHERE nse.surname LIKE %s;
            """, (searcht,))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0],cur.fetchone()[1],cur.fetchone()[2],cur.fetchone()[3],cur.fetchone()[6])
    cur.execute("""
            SELECT * FROM name_surname_email AS nse
            LEFT JOIN numbers AS n ON nse.id_client = n.id_name
            WHERE nse.email LIKE %s;
            """, (searcht,))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0],cur.fetchone()[1],cur.fetchone()[2],cur.fetchone()[3],cur.fetchone()[6])
    cur.execute("""
            SELECT * FROM name_surname_email AS nse
            LEFT JOIN numbers AS n ON nse.id_client = n.id_name 
            WHERE n.number LIKE %s;
            """, (searcht,))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0],cur.fetchone()[1],cur.fetchone()[2],cur.fetchone()[3],cur.fetchone()[6])



#запуск кода
if __name__ == '__main__':
    with psycopg2.connect(database="", user="", password="") as conn:
        with conn.cursor() as cur:
# запуск функциий
            #new_table() # создание таблиц
            #del_table() # Удаление таблиц
            #new_client( 'lef', 'LLef', 'dsfsdf', 45834534) #заполнение таблиц
            #add_nub(1, 34234) # Добавление номера существующего клиента
            #change_data(2, 'gd1fg', 'susd111f1rn', 'ems2d12f', 9943204) #изменение данных клиента
            #change_phone(1, 46664564) # изменение номера телефона
            #del_pnones(2,'9943204')# удаление номера телефона
            #del_client(4) #Функция, позволяющая удалить существующего клиента
            #search('45834534') #Поиск клиента

conn.close()
