import requests
import geocoder


def map_parameters(ll, spn):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        "pt": "{0},pm2dgl".format(ll)
    }
    return map_params


def make_map(map_params):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def search(toponym):
    ll, spn = geocoder.get_ll_spn(toponym)
    map_params = map_parameters(ll, spn)
    make_map(map_params)
