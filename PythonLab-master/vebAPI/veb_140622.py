import requests
import json
from test_config import fix


def test1():
    assert 25 == 25


def test2():
    assert 1 in [1, 2, 3]


def test2n():
    assert 1 in [2, 3]


def test3():
    assert 'a' in ('a', 'b')


def test3n():
    assert 'a' in ('c', 'b')


def test4n():
    assert 15 == 16


def test_add_pet():
    input_pet = {
        "id": 213,
        "category": {
            "id": 25,
            "name": "Vrapp"
        },
        "name": "BOOGY",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    assert res_get.status_code == 200
    assert json.loads(res_get.text) == input_pet


def test_sold_list():
    input_pet = {
        "id": 215,
        "category": {
            "id": 25,
            "name": "Snoopy"
        },
        "name": "Alien",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "sold"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'sold'})

    assert res_get.status_code == 200
    assert list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))


def test_add_other():
    input_pet = {
        "id": 228,
        "category": {
            "id": 25,
            "name": "Flap"
        },
        "name": "Morlok",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "Flap"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'available'})

    assert res_get.status_code == 200
    assert list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))


def test_add_pet_neg():
    input_pet = {
        "id": 219,
        "category": {
            "id": 25,
            "name": "Vrapp"
        },
        "name": "BOOGY",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/45654687987987')

    assert res_get.status_code == 404
    # assert json.loads(res_get.text) == input_pet


def test_del_pet():
    input_pet = {
        "id": 219,
        "category": {
            "id": 25,
            "name": "Vrapp"
        },
        "name": "BOOGY",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 14,
                "name": "string"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_del = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    out_del = {
        "code": 200,
        "type": "unknown",
        "message": "219"
    }
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
    assert res_del.status_code == 200
    assert json.loads(res_del.text) == out_del
    assert res_get.status_code == 404
    # assert json.loads(res_del.text) == input_pet


def test_add_pet_conf(fix):
    input_pet, header = fix
    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    assert res_get.status_code == 200
    assert json.loads(res_get.text) == input_pet
    res_del = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    out_del = {
        "code": 200,
        "type": "unknown",
        "message": "219"
    }
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')
    assert res_del.status_code == 200
    assert json.loads(res_del.text) == out_del
    assert res_get.status_code == 404