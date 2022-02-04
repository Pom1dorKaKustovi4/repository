import requests

APIKEY = "40d1649f-0493-4b70-98ba-98533de7710b"


def geocoder(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": APIKEY,
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def get_coordinates(address):
    toponym = geocoder(address)
    coordinates = toponym['Point']['pos']
    longitude, lattitude = map(float, coordinates.split(' '))
    return longitude, lattitude


def get_ll_spn(address):
    toponym = geocoder(address)
    lon, lat = get_coordinates(address)
    ll = ','.join(map(str, [lon, lat]))
    envelope = toponym['boundedBy']['Envelope']
    left, bottom = envelope['lowerCorner'].split(' ')
    right, top = envelope['upperCorner'].split(' ')
    lon = abs(float(left) - float(right))
    lat = abs(float(bottom) - float(top))
    spn = f'{lon},{lat}'
    return ll, spn
