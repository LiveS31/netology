import configparser
config = configparser.ConfigParser()
config.read('.pass.ini')


import vk_api, vk
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

#vk_session = vk_api.VkApi(token= config['vk']['KEY_GROUP'])
session = vk.Sesion(access_token = config['vk']['KEY_GROUP'])
#longpoll = VkBotLongPoll(vk_session, '219698123')
session = vk.Session()
vk_api=vk.API(session)
vk_api.users.get(user_id=1)
