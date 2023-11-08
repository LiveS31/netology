import pytest
from django.contrib.auth.models import User
# Импортирурум для возмодности корректно импортировать сервисы в API клиента
from rest_framework.test import APIClient
from model_bakery import baker #с помощью создаем объект

from testing.drf_test.demo.models import Message


#from .models import Message


@pytest.fixture
#данная функция являет текстурой и служит для того, чтобы не дублировался код

def client():
    return APIClient()

# создаем текстуру, которая будет создавать новых пользователей
@pytest.fixture
#функция вернет свежесозданного пользователя
def user():
    return User.objects.create_user('admin')

#фабрика объектов
@pytest.fixture
def message_factory():
    def factory(*args, **kwargs): # дополнительные параметры *args, **kwargs
        return baker.make(Message, *args, **kwargs)#параметры будут сообщения
        # и дополнительные параметры

    return factory



@pytest.mark.django_db #запускаем тест и говорим,
# что будет использоваться база данных. Декоратор нужен,
# чтобы корректно отработал тест
def test_get_messages(client, user, message_factory):
    # есть три секции

    # Arrange - подготовка данных
    messages = message_factory(_quantity=10)# передаем сюда параметры сколько нужно

    # Act - непосредственно тестируемый функционал
    #вызов того или иного метода
    response = client.get('/messages/')# отправляем сообщение клиенту

    # Assert - проверка того, что действие выполнено корректно
    assert response.status_code == 200 #проверяем, что наш статус код = 200
    data = response.json()#сохраняем ответ в переменную data в формате json
    assert len(data) == len(messages) #длинна данных в базе должн быть
    #равна длинне получаемого сообщения
    for i, m in enumerate(data):#получаем индексы сообщении
        assert m['text'] == messages[i].text# проверим, что они действительно равны


@pytest.mark.django_db#запускаем текст и говорим что будет использоваться база данных
def test_create_message(client, user):
    count = Message.objects.count() #узнаем сколько в нашей базе данных сообщений
#отправляем текст сообщения - в data прописываем все остальное
    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})
#проверяем, что код выполнен корректно
    assert response.status_code == 201 #код при сохранении объекта = 201
# проверяем, что действительно сообщению добавилось и их стало на больш
    assert Message.objects.count() == count + 1 # на одно сообщение больше
