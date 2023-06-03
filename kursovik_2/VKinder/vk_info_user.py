from settings import TOKEN_VK, KEY_GROUP
import vk_api


def get_info_users(id_user):
    """Gets the necessary information about users."""
    id_user = id_user
    vk = vk_api.VkApi(token=KEY_GROUP)
    response = vk.method('users.get', {'user_ids': id_user, 'fields': 'city, sex, bdate'})
    try:
        user_info = [response[0]['id'], response[0]['first_name'], response[0]['last_name'],
                     response[0]['sex'], response[0]['city']['title'], f'https://vk.com/id{response[0]["id"]}']
        return user_info
    except KeyError:
        user_info = [response[0]['id'], response[0]['first_name'], response[0]['last_name'],
                     response[0]['sex'], None, f'https://vk.com/id{response[0]["id"]}']
        return user_info


def search_users(sex, age_from, age_to, city):
    """Search for users by the specified parameters."""
    all_persons = []
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token=TOKEN_VK)
    response = vk.method('users.search',
                         {'sort': 1,
                          'sex': sex,
                          'status': 1,
                          'age_from': age_from,
                          'age_to': age_to,
                          'has_photo': 1,
                          'count': 25,
                          'online': 1,
                          'hometown': city
                          })
    for element in response['items']:
        person = [
            element['first_name'],
            element['last_name'],
            link_profile + str(element['id']),
            element['id']
        ]
        all_persons.append(person)
    return all_persons


def get_photo(owner_id):
    """Gets users photos."""
    try:
        vk = vk_api.VkApi(token=TOKEN_VK)
        response = vk.method('photos.get',
                             {'owner_id': owner_id,
                              'album_id': 'profile',
                              'count': 10,
                              'extended': 1,
                              'photo_sizes': 1})
        users_photos = []
        for i in range(len(response['items'])):
            users_photos.append(
                [response['items'][i]['likes']['count'],
                 response['items'][i]['sizes'][-1]['url']])
        return users_photos
    except(vk_api.exceptions.ApiError, TypeError):
        pass


def sort_photo(photo_list):
    """Sorts users' photos."""
    try:
        sort_list = sorted(photo_list, key=lambda x: int(x[0]), reverse=True)
        return sort_list[:3]
    except(vk_api.exceptions.ApiError, TypeError):
        return ['нет фото']
