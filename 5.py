import sys
import requests
import geocoder

ll, spn = geocoder.get_ll_spn(" ".join(sys.argv[1:]))

map_params = {
    "ll": ll,
    "spn": spn,
    "l": "map",
    "pt": "{0},pm2dgl".format(ll)
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
