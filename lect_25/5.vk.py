import requests         # делать http-запросы
import time             # делать задержки тобы не забанили
from tqdm import tqdm   # progress bar

HOST = 'https://api.vk.com/method'
VERSION = '5.74'
access_token = 'TOKEN HERE'

# пример запроса
r = requests.get(HOST + 'users.get', params={'user_ids': '1699912,1',
                                             'access_token': access_token,
                                             'v': VERSION})

r.json()['response'][0] # инфа о первом юзере


# ищем связь между пользователями
id_start = 111900610
id_end = 1699912

def get_friends_list(id_user):
    r = requests.get(HOST + 'friends.get', params={'user_id': id_user,
                                                   'access_token': access_token,
                                                   'v': VERSION})
    if 'response' in r.json():
        return r.json()['response']['items']

# строим цепочку друзей
from collections import deque
queue = deque(get_friends_list([id_start]))

distances = {v: 1 for v in queue}
parents = {v: id_start for v in queue}
parents[id_start] = None

while id_end not in distances:
    cur_user = queue.popleft()
    new_users = get_friends_list(cur_user)
    time.sleep(0.2)
    for u in tqdm(new_users):
        if u not in distances:
            queue.append(u)
            distances[u] = distances[cur_user] + 1
            parents[u] = cur_user

path = [id_end]
parent = parents[id_end]
while not parent is None:
    path.append(parent)
    parent = parents[parent]