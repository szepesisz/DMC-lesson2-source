import base64
from urllib.request import urlopen
import requests
from posixpath import join as urljoin


def task_1():
    url_base = 'https://www.random.org/'
    service = 'integers'
    params = '/?num=1&min=1&max=10000&col=1&base=10&format=plain&rnd=new'
    with urlopen(url_base + service + params) as r:
        ret = r.read().decode('utf-8')
    print(int(ret))


def task_2():
    def randint(a, b):
        url_base = 'https://www.random.org/'
        service = 'integers'
        params = f'/?num=1&min={a}&max={b}&col=1&base=10&format=plain&rnd=new'
        with urlopen(url_base + service + params) as r:
            ret = r.read().decode('utf-8')
        return int(ret)

    print(randint(0, 10))
    print(randint(0, 10))


def task_3():
    def randint(a, b):
        url_base = 'https://www.random.org'
        path = 'integers'
        r = requests.get(
            urljoin(url_base, path),
            params=dict(
                num=1, min=a, max=b, col=1, base=10, format='plain', rnd='new'
            )
        )
        return int(r.content)

    print(randint(1, 100))

    # feladat: random.choice implementálása


def task_4():
    r = requests.get('https://api.adviceslip.com/advice')
    print(r.content)
    print(r.json())
    advice = r.json()
    print(type(advice))

    r = requests.get('https://api.adviceslip.com/advice/42')
    print(r.json())

    r = requests.get('https://api.adviceslip.com/advice/search/car')
    print(r.json())


def task_5():
    label = 'kutya'
    access_key = '85b9b293c84910a3d9f087dbf8b86802'
    url = 'https://moly.hu/api/books.json'
    r = requests.get(
        url=url,
        params=dict(
            q=label,
            key=access_key
        )
    )
    print(r.json())


def task_6():
    CLIENT_ID = 'bbc4b3b81dbe40cdbb6e69476267adc0'
    CLIENT_SECRET = '65516cac54df4e96a435ea318223fcea'

    artist = 'Krúbi'

    r = requests.post(
        url='https://accounts.spotify.com/api/token',
        headers={
            'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode(),
        },
        data={'grant_type': 'client_credentials'}
    )
    print(r.status_code)
    token = r.json()['access_token']
    # print(token)
    artists = []
    resp = requests.get(
        url='https://api.spotify.com/v1/search',
        params={'q': f'artist:{artist}', 'type': 'artist', 'limit': 10},
        headers={'Authorization': f'Bearer {token}'}
    ).json()
    for a in resp['artists']['items']:
        artists.append({'id': a['id'], 'name': a['name']})

    artist = artists[0]
    print(artists)

    r = requests.get(
        url='https://api.spotify.com/v1/artists/{id}/albums'.format(id=artist['id']),
        params=dict(
            limit=50
        ),
        headers={'Authorization': f'Bearer {token}'}
    )
    albums = r.json()['items']
    print(albums)
    for a in albums:
        print(a['name'])
        print('\t->', a['album_type'], a['album_group'])


def task_7():
    CLIENT_ID = 'bbc4b3b81dbe40cdbb6e69476267adc0'
    CLIENT_SECRET = '65516cac54df4e96a435ea318223fcea'

    s = requests.session()
    r = s.post(
        url='https://accounts.spotify.com/api/token',
        headers={
            'Authorization': 'Basic ' + base64.b64encode(f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()).decode(),
        },
        data={'grant_type': 'client_credentials'})

    s.headers['Authorization'] = f'Bearer {r.json()["access_token"]}'

    artist = 'Sisi'

    r = s.get(
        url='https://api.spotify.com/v1/search',
        params={'q': f'artist:{artist}', 'type': 'artist', 'limit': 10},
    )
    print(r.json())
    a_id = r.json()['artists']['items'][0]['id']
    r = s.get(
        url='https://api.spotify.com/v1/artists/{id}/albums'.format(id=a_id),
        params=dict(
            limit=50
        ),
    )
    albums = r.json()['items']
    print(albums)
    for a in albums:
        print(a['name'])
        print('\t->', a['album_type'], a['album_group'])


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    task_6()
    # task_7()
