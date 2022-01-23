from pprint import pprint

import requests

diary = {}


def test_request(hero_name):
    iq_number = 0
    for i in hero_name:
        url = "https://superheroapi.com/api/2619421814940190/search/" + i
        response = requests.get(url)
        data = response.json()
        upd_data = int(data['results'][0]['powerstats']['intelligence'])
        if upd_data > iq_number or upd_data == iq_number:
            diary[i] = upd_data
            iq_number = upd_data

    for k, v in diary.items():
        if v == iq_number:
            print(f"{k} has the most intelligence. It is equal to {v}.")


test_request(['Hulk', 'Captain America', 'Thanos'])
