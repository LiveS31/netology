import requests

token_ya = ''

def get_headers(token): #создаем аторизацию (токен и все дела)
    return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
            }
def get_foldres(): # Создаем папку на Ya диске
    foldres = 'new_foldres' #название папки
    file_url = 'https://cloud-api.yandex.net/v1/disk/resources/' # путь
    headers = get_headers(token_ya) #передаем токен
    res_d = requests.delete(f'{file_url}?path={foldres}',headers=headers) #удаление папки
    #print(res_d.status_code)
    res_c = requests.put(f'{file_url}?path={foldres}',headers=headers) # сам запрос

    #print(res_c.status_code)
    return res_c.status_code

get_foldres()
