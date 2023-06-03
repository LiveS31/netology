from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from db_functions import add_user, add_user_profile, add_photo, check_db_favorites, add_black_user_profile, \
    check_db_black
from vk_info_user import search_users, get_photo, sort_photo, get_info_users
from settings import KEY_GROUP


def get_long_poll(token):
    """Gets a token for interacting with the server."""
    vk = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk)
    return longpoll


def loop_bot():
    """Gets the user id and message text."""
    for event in get_long_poll(KEY_GROUP).listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                message_text = event.text.lower()
                return message_text, event.user_id


def menu_bot(id_num):
    """Bot's response."""
    write_msg(id_num,
              f"\nВас приветствует бот - Vkinder!\n"
              f"Вам одиноко?\n"
              f" Хотите найти пару?\n"
              f"Или надумали познакомиться с избранными?\n"
              f"Введите: Да или Нет.\n")


def menu_bot_2(id_num):
    """Bot's response."""
    write_msg(id_num,
              f"\nДля поиска введите пол, границы возраста и город\n"
              f"Например, девушка 18-25 Москва\n"
              f"Перейти в избранное - 2\n"
              f"Перейти в черный список - 0\n")


def menu_bot_3(id_num):
    """Bot's response."""
    write_msg(id_num,
              f'\nЭто была последняя анкета.\n'
              f'Основное меню - привет\n')


def write_msg(user_id, message, attachment=None):
    vk_api.VkApi(token=KEY_GROUP).method('messages.send',
                                         {'user_id': user_id,
                                          'message': message,
                                          'attachment': attachment,
                                          'random_id': randrange(10 ** 7)
                                          })


def menu():
    """Interacts with the bot."""
    while True:
        msg_text, user_id = loop_bot()
        if msg_text == 'привет':
            menu_bot(user_id)
            msg_text, user_id = loop_bot()
            if msg_text.lower() == 'да':
                add_user(user_id)
                menu_bot_2(user_id)
                msg_text, user_id = loop_bot()
                if len(msg_text) > 1:
                    sex = 0
                    if msg_text.split()[0].lower() in ['женщина', 'девушка']:
                        sex = 1
                    elif msg_text.split()[0].lower() in ['мужчина', 'парень']:
                        sex = 2
                    age_from = msg_text.split()[1][0:2]
                    if int(age_from) < 18:
                        write_msg(user_id, 'Минимальный возраст - 18 лет.')
                        age_from = 18
                    age_to = msg_text.split()[1][3:]
                    if int(age_to) >= 100:
                        write_msg(user_id, 'Максимальный возраст 99 лет.')
                        age_to = 99
                    city = msg_text.split()[2].lower()
                    result = search_users(sex, int(age_from), int(age_to), city)
                    # create_json(result)
                    for i in range(25):
                        user_photo = get_photo(result[i][3])
                        print (i)
                        sorted_user_photo = sort_photo(user_photo)
                        write_msg(user_id, f'\n{result[i][0]}  {result[i][1]}   {result[i][2]}')
                        if user_photo == True:
                            write_msg(user_id,
                                      f'фото: ',
                                      attachment=','.join([sorted_user_photo[-1][1],
                                                           sorted_user_photo[-2][1],
                                                           sorted_user_photo[-3][1]]))
                        #except IndexError:
                        else:
                            for photo in range(len(sorted_user_photo)):
                                write_msg(user_id,
                                          f'фото: ',
                                          attachment=sorted_user_photo[photo][1])
                        write_msg(user_id, '1 - Добавить, 2 - Заблокировать, 0 - Далее, \nВыход - выход из поиска')
                        msg_text, user_id = loop_bot()
                        if msg_text == '0':
                            if i >= len(result) - 1:
                                menu_bot_3(user_id)
                        elif msg_text == '1':
                            user_profile = get_info_users(result[i][3])
                            add_user_profile(user_profile, user_id)
                            if sorted_user_photo == ['нет фото']:
                                pass
                            else:
                                add_photo(result[i][3])
                        elif msg_text == '2':
                            user_profile = get_info_users(result[i][3])
                            add_black_user_profile(user_profile, user_id)
                        elif msg_text.lower() == 'выход':
                            write_msg(user_id, 'Для активации бота введите: Привет')
                            break
                elif msg_text == '2':
                    profile = check_db_favorites(user_id)
                    write_msg(user_id, 'Анкеты избранного: ')
                    for i in profile:
                        write_msg(user_id, f'{i.first_name} {i.last_name}, {i.link}')
                    write_msg(user_id, 'Основное меню - привет')
                elif msg_text == '0':
                    profile = check_db_black(user_id)
                    write_msg(user_id, 'Анкеты черного списка: ')
                    for i in profile:
                        write_msg(user_id, f'{i.first_name} {i.last_name}, {i.link}')
                    write_msg(user_id, 'Основное меню - привет')
            else:
                write_msg(user_id,
                          f"\nОчень жаль. До свидания.")
                break
        else:
            write_msg(user_id,
                      f"\nДля активации бота введите: Привет")
