import requests

'''
Этот код выполняет запрос к API Википедии для поиска географических объектов (мест) вблизи заданных координат. 
Создаем сессию requests.Session(). Сессия позволяет сохранять параметры между запросами и поддерживать подключение к серверу.
'''
S = requests.Session()


def get_sites(lat, long, radius, limit=100):
    """
    Установка URL и параметров запроса:
    - url указывает на API Википедии (https://en.wikipedia.org/w/api.php).
    - params — словарь с параметрами запроса:
        -"format": "json": формат ответа — JSON.
        - "list": "geosearch": используем метод geosearch для поиска географических объектов.
        - "gscoord": "37.7891838|-122.4033522": координаты для поиска (широта и долгота).
        - "gslimit": "10": максимальное количество результатов — 10.
        - "gsradius": "10000": радиус поиска в метрах — 10 000 метров (10 км).
        - "action": "query": тип действия — запрос.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }
    """
    Выполняем GET-запрос к API Википедии с указанными параметрами.
    Результат запроса сохраняется в переменную r.
    Преобразуем ответ в формат JSON с помощью метода .json(), затем извлекаем список найденных объектов из ответа API.
    Возвращаем полный список найденных объектов sites.
    """
    r = S.get(url=url, params=params)
    pages = r.json()['query']['geosearch']
    sites = [i['title'] for i in pages]
    return sites


def test_san_fran_sites(san_fran_coord, san_fran_text):
    assert san_fran_text in get_sites(san_fran_coord[0], san_fran_coord[1], 100), 'Not found'


def test_moscow_sites(moscow_coord, moscow_text):
    assert moscow_text in get_sites(moscow_coord[0], moscow_coord[1], 100), 'Not found'
