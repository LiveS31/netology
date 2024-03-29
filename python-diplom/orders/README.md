**Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».**

## Информация о работе



Документация по запросам Postman:
- https://documenter.getpostman.com/view/7714993/SzzegzeB?version=latest

Если требуется создать базу данных:
- выполнить файл base.py
  (и заменить данные в файле settings.py. по умолчанию используется sqlite )

Чтобы запустить сервер:
- pip install -r requirements.txt (желательно в виртуальной среде) 
- python manage.py migrate
- python manage.py makemigrations
  Добавить суперпользователя:
  python manage.py createsuperuser:
  email: admin@admin.com
  password: admin
- python manage.py runserver

## Описание

Приложение предназначено для автоматизации закупок в розничной сети. Пользователи сервиса — покупатель (менеджер торговой сети, который закупает товары для продажи в магазине) и поставщик товаров.

**Клиент (покупатель):**

- Менеджер закупок через API делает ежедневные закупки по каталогу, в котором
  представлены товары от нескольких поставщиков.
- В одном заказе можно указать товары от разных поставщиков — это
  повлияет на стоимость доставки.
- Пользователь может авторизоваться, регистрироваться и восстанавливать пароль через API.
    
**Поставщик:**

- Через API информирует сервис об обновлении прайса.
- Может включать и отключать прием заказов.
- Может получать список оформленных заказов (с товарами из его прайса).


### Задача

Необходимо разработать backend-часть (Django) сервиса заказа товаров для розничных сетей.

**Базовая часть:**
* Разработка сервиса под готовую спецификацию (API);
* Возможность добавления настраиваемых полей (характеристик) товаров;
* Импорт товаров;
* Отправка накладной на email администратора (для исполнения заказа);
* Отправка заказа на email клиента (подтверждение приема заказа).
