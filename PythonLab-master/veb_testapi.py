import pytest
import requests
import json


class TestAPI:

    def test_select_pet(self):
        url = "http://130.193.37.179/api/pet/517d137a-d05e-48bc-b1c0-cfeb09e06f23/"
        response = requests.get(url)

        print(response.text)
        print(response.status_code)
        print(json.dumps(response.text, indent=4, sort_keys=True))

# 19-50 Вебинар-практикум по автоматизированному тестированию 24.01.2022
