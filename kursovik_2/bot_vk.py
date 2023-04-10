from random import randrange
import configparser
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
config = configparser.ConfigParser()
config.read('.pass.ini')
#token = config['vk']['KEY_GROUP']#input('Token: ')



vk = vk_api.VkApi(token=config['vk']['KEY_GROUP'])
longpoll = VkLongPoll(vk, 219698123)
vk = vk.get_api()
print (vk)

def keybord():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Поиск участника', color=VkKeyboardColor.POSITIVE)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text
            print(event.text)

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == 'Поиск участника':
                write_msg(event.user_id,
                          'JKFb',
                    keyboard=create_keyboard()
                )

           # else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")