
import configparser
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api#, vk
from vk_api.utils import get_random_id

config = configparser.ConfigParser()
config.read('.pass.ini')

vk_sesion = vk_api.VkApi(token= config['vk']['KEY_GROUP'])

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_sesion, 219698123)
#vk = vk_sesion.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_sesion)
Lsvk = vk_sesion.get_api()

from vk_info_user import search_users, get_info_users, create_json
user_seach = []
class VK_bot:
    def __init__(self):
        self.lslongpoll = Lslongpoll
        self.lsvk = Lsvk
        self.longpoll = longpoll
        self.VkEventType = VkEventType
        self.keyboard = VkKeyboard(one_time=True)

#бот
    def message_user(self):
        user_seach = []
        self.keyboard.add_button(label='Поиск участника', color=VkKeyboardColor.POSITIVE)
        self.keyboard.add_button('Поиск Х участника', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_button('Просмотр участника', color=VkKeyboardColor.PRIMARY)
        self.keyboard.add_line()
        self.keyboard.add_button('Запись в базу', color=VkKeyboardColor.NEGATIVE)
        self.keyboard.add_line()
        self.keyboard.add_location_button()

        for event in self.lslongpoll.listen():
            if event.type == self.VkEventType.MESSAGE_NEW and event.to_me and event.text:
                #print(event.attachments)
                var1 = ['привет','g']
                if event.text in var1:
                    if event.from_user:
                        self.lsvk.messages.send(
                            user_id = event.user_id,
                            random_id = get_random_id(),
                            message = 'Привет)'#,
                            #user_1 = event.attachments
                        )

                vars2 = ['клава', 'r']
                if event.text in vars2:
                    #if event.from_user:
                    self.lsvk.messages.send(
                                user_id = event.user_id,
                                random_id = get_random_id(),
                                keyboard = self.keyboard.get_keyboard(),
                                message = 'А вот'
                            )

                if event.text == 'Поиск участника':

                        self.lsvk.messages.send(
                        user_id = event.user_id,
                        random_id = get_random_id(),
                        message = 'Запуск\nПол, возраст,город\n Через пробел'
                                                )
                        user_seach.append(event.message)


                print (user_seach)
                    #create_json(search_users(2, 18, 40, 'Санкт-Петербург'))

                    #search_users(sex=None, age_from=None,age_to=None, city=None)
        print (user_seach)

        return #tema# vk_bot.keyboard()

    def search(self, s=None, d=None, f=None, g=None):
        search_users(s, d, f, g)

if __name__ == "__main__":
    vk_bot = VK_bot()
    vk_bot.message_user()

