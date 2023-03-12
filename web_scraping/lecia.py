# <div class="ip" id="d_clip_button" style="cursor: pointer;">
#                                     <span>109.252.24.65</span>
#
#                                     <i class="ip-icon-shape btn-copy"></i>
#                                 </div>
# сайт в коде если на сайте нет защиты
import requests
#HOST = 'http://kafeantrakt.com/'
# html = requests.get(HOST).text
# print (html)
# если сайт с защитой
from fake_headers import Headers # позволяет имитировать для сайта любой браузер
#нужно создать экземпляр класса и записать туда заголовки
# headers = Headers(browser='firefox', os='win').generate()
HOST = 'https://2ip.ru'
# html = requests.get(HOST, headers=headers).text
# print (html)
# если защита еще круче

#webdriver_manager - автоматически настраивает окружение
from selenium import webdriver #(через веб драйвер будет отправлять запросы)
from webdriver_manager.chrome import ChromeDriverManager # автоматически подготовит
# всю среду для запросов
from selenium.webdriver.chrome.service import Service as ChromeService # можно было не присваивать
# создаем среду и передаем туда данные которые сгенерит driver_manager

# если нужно добавить ожидания элемента
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


# #   устанавливаем двигатель селениюм
# service = ChromeService(executable_path=ChromeDriverManager().install())
# # создаем экземпляр драйвера класса хрома и можем посещать какую либо страницу
# driver = webdriver.Chrome(service=service)
# driver.get(HOST)
# # Найти эл# делаем поиск по данному классу (добавится переменная element
# element = driver.find_element(value='d_clip_button')
# # определили , что в переменной ip леит в значении text
# # извекаем
# ip = element.text
# idi = element.id
# print(driver)
#
# #сама функция ожидания
# def wait_element(driver, delay_seconds=1, by=By.TAG_NAME, value= None):
#     '''
#     Иногда элементы на странице не прогружаются сразу
#     функция ждет delay_seconds если элемент еще не прогрузился
#     Если за отведенное время элемент не прогружается выбрасывается TmeoutException
#     :param driver:
#     :param delay_seconds:
#     :param by:
#     :param value:
#     :return:
#     '''
#     return WebDriverWait(driver, delay_seconds).until(
#         expected_conditions.presence_of_element_located((by, value)))
# # как ожидать по элементу
# element = wait_element(driver, delay_seconds=10, by=By.ID, value='d_clip_button')
# # где delay_seconds - сколько ожидать
# # by=By.ID - по какому элементу ожидать
# # value = в каком ключе искать ожидаемый элелмент
###########
#копируем и забираем
###########
#<span class="tm-article-datetime-published"><time
# datetime="2023-03-12T11:05:36.000Z"
# title="2023-03-12, 14:05">50 минут назад</time></span>
import requests
#импортируем фейковые заголовки
from fake_headers import Headers
from bs4 import BeautifulSoup

# имя переменной
HOST = 'https://habr.com'
# главная страница
MAIN = f'{HOST}/ru/all'
# генерация фейковых заголовках делаем в функции
def get_headers():
    return Headers(browser='firefox', os = 'win').generate()

# извлечем главную страницу
main_page = requests.get(MAIN, headers=get_headers()).text
# там где статья на данном сайте
#<div class="article-formatted-body article-formatted-body article-formatted-body_version-2"><p>
# Нас окружает целый зоопарк электронных помощников, которые позволяют нам сохранять почти неограниченный объём заметок
# и записок. Однако мне кажется, что удобно и практично, а в некоторых случаях и куда более безопасно помнить наизусть
# то, чем пользуешься каждый день.</p><p>Метод мнемонических правил можно использовать не только для запоминания нужных
# цифр и объектов, но и для генерации последовательностей по определённым правилам. Почему бы не внести в окружающую
# действительность толику безбашенного сюрреализма, сочиняя всякие мнемоники и совмещая забавное
# с полезным?</p><p></p></div>
bs = BeautifulSoup(main_page, features= 'lxml')
#parser= 'lxml' - кодировка для страницы
articles_list = bs.find(class_='tm-articles-list')
#получить все теги с article
articles_tags = articles_list.find_all('article')
# вытаскиваем данные и помещаем их в словарь

parser_data = []

for article_tag in articles_tags:
    time_tag = article_tag.find('time')
    time = time_tag['datetime']
    title = article_tag.find('h2').find('span').text
    link = article_tag.find('a', class_= 'tm-article-snippet__title-link')['href']
    link = f'{HOST}{link}'
    # parser_data.append({
    #     'time': time,
    #     'title': title,
    #     'link:': link
    # })
#извлекаем текст статьи
    full_article_html = requests.get(link, headers=get_headers()).text
    full_articles_bs = BeautifulSoup(full_article_html, features='lxml')
    full_articles_tag = full_articles_bs.find(class_='tm-article-body')
    text = full_articles_tag.text

    parser_data.append({
        'time': time,
        'title': title,
        'link:': link,
        'text': text
    })

print(parser_data)
#print(articles_list)

#print (main_page)
