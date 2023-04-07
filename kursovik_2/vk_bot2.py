# from random import randrange
# import configparser
#
# from vk_api import keyboard
# from vk_api.keyboard import VkKeyboard, VkKeyboardColor
# import vk_api, vk
# from vk_api.utils import get_random_id
# #from vk_api.longpoll import VkLongPoll, VkEventType
# config = configparser.ConfigParser()
# config.read('.pass.ini')
#
# vk_sesion = vk_api.VkApi(token= config['vk']['KEY_GROUP'])
#
# from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
# #longpoll = VkBotLongPoll(vk_sesion, 219698123)
# #vk = vk_sesion.get_api()
# from vk_api.longpoll import VkLongPoll, VkEventType
# Lslongpoll = VkLongPoll(vk_sesion)
# Lsvk = vk_sesion.get_api()
# user_mes = []
# keyboard = VkKeyboard(one_time=True)
# #кнопк
#
#
# keyboard.add_button('Поиск участника', color=VkKeyboardColor.POSITIVE)
# keyboard.add_button('Поиск Х участника', color=VkKeyboardColor.PRIMARY)
# keyboard.add_button('Просмотр участника', color=VkKeyboardColor.PRIMARY)
# keyboard.add_line()
# keyboard.add_button('Запись в базу', color=VkKeyboardColor.NEGATIVE)
# keyboard.add_line()
# keyboard.add_location_button()
#
# # прием - отправка
#
#
# for event in Lslongpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
#         vars1 = ['привет', 'хай']
#         if event.text in vars1:
#             if event.from_user:
#                 Lsvk.messages.send(
#                     user_id = event.user_id,
#                     message = 'Привет)',
#                     random_id = get_random_id()
#                     )
#         vars2 = ['клава', 'к']
#         if event.text in vars2:
#             if event.from_user:
#                 Lsvk.messages.send(
#                     user_id = event.user_id,
#                     random_id = get_random_id(),
#                     keyboard = keyboard.get_keyboard(),
#                     message = 'А вот'
#                     )
#         #var3 = ['Запись в базу','Поиск участника','Просмотр участника']
#
#         if event.text == 'Запись в базу':
#             user_mes.append(f'{event.user_id} = Требуется запись')
#         elif event.text == 'Поиск Х участника':
#             Lsvk.messages.send(
#                 user_id=event.user_id,
#                 random_id=get_random_id(),
#                 message='Введите ID пользователя или его имя'
#                 )
#             user_mes.append(event.text)
#             print(user_mes, '1111')
#         # elif event.text =='Поиск участника'
#         # elif event.text == 'Просмотр участника'
#         #print(user_mes)
#
#         print (f'ID User - {event.user_id}\nMessage - {event.text}')
#
