import pytest
from django.contrib.auth.models import User
#Импортируем для возможности корректно импортировать сервисы API
from rest_framework.test import APIClient
#создаем c данным импортом объект
from model_bakery import baker #с помощью создаем объект(библиотека рандомных данных)
from django.urls import reverse #делает типа url
from students.models import Course, Student


# def test_example():
#     assert False, "Just test example"
@pytest.fixture
#создаем текстуру для уменьшения кода
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):#создаем дополнительные параметры (*args, **kwargs)
        return baker.make(Course, *args, **kwargs) #параметры будут course
    #+ дополнительные параметры
    return factory
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
#запускаем тест db - будет использоваться база данных
def test_course(client, course_factory):
    courses = course_factory(_quantity=3) #счетчик
    URL = reverse('courses-detail', args=[courses[0].id])
    response = client.get(URL) #отправляем на запрос по адресу (ну и получаем твет)
    assert response.status_code == 200 # проверка корректности
    assert response.data['id'] == courses[0].id # проверка соответствия

@pytest.mark.django_db
def test_course_list(client, course_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-list') # = f'/api/v1/courses/' -так везде
    response = client.get(URL)
    assert response.status_code == 200
    for i, v in enumerate(response.data): #получаем индексы
        assert v['name'] == course[i].name # сравниваем

@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', {'id':course[0].id})
    assert response.status_code == 200
    assert response.data[0]['id'] == course[0].id

@pytest.mark.django_db
def test_course_filter_name(client, course_factory, student_factory):
    course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/', {'name':course[1].name})
    assert response.status_code == 200
    assert response.data[0]['name'] == course[1].name

@pytest.mark.django_db
def test_create_course(client):
    URL = reverse('courses-list')
    response = client.post(URL,{'name': 'biology'}) # отправляем данные
    assert response.status_code == 201
    assert response.data['name'] == 'biology'

@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-detail', args=[course[1].id])
    response = client.patch(URL, {'name':'math'}) #проверяем изменения
    assert response.status_code == 200
    assert response.data['name'] == 'math'

@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    course = course_factory(_quantity=5)
    URL = reverse('courses-detail', args=[course[0].id])
    response = client.delete(URL)
    assert response.status_code == 204
    assert response.data is None
