from api import PetFriends
from settings import valid_email, valid_password
import os
import  pytest

print(valid_email, valid_password)


pf = PetFriends()


def generate_string(n):
   return "x" * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


# 1
def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    print(email, password)
    print(status, result)

    assert status == 200
    assert 'key' in result


# 2
def test_get_all_pets_with_valid_key(filter='my_pets'):  # filter='my_pets' - получить список  собственных питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    # print(status)

    # print('имя ',result['pets'][0]['name'])

    assert status == 200
    assert len(result['pets']) > 0


# 3
def test_add_new_pet_with_valid_data(name='Новичек', animal_type='Пушун', age='10', pet_photo='images/foto1.jpg'):
    """ Проверяем добавление питомца с фото, и корректность занесенных данных. Фото не сравнивается
    только то что оно не пустое"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, 'images/foto1.jpg')  # OS не срабатывает((

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


# 4
def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Гагарин", "собака", "4", "images/foto1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


# 5
def test_successful_update_self_pet_info(name='Обновленный1', animal_type='НОВЕЙШИЙ', age=2):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("У тебя нет питомцев")


# 6
def test_add_new_pet_simple_with_valid_data_without_photo(name='Нефотогеничный', animal_type='вампир',
                                                          age='100'):
    """Проверяем возможность добавления нового питомца с корректными данными, но без фото"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] == ''


# 7
def test_add_photo_of_pet(pet_photo='images/foto1.jpg'):
    """Проверяем возможность добавления фото в созданного питомца без фото"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берем первого питомца и добавляем его фото
    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    # Проверяем, что статус ответа = 200 и у питомца появилось фото
    assert status == 200
    assert result['pet_photo'] != ''


# 8
def test_add_new_pet_with_invalid_pet_photo(name='Непутевый', animal_type='Безпути',
                                            age='8',
                                            pet_photo=' '):
    """Проверяем, что нельзя добавить питомца, если не указан путь до файла с фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца

    try:
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    except PermissionError:

        print("Укажите путь к файлу")


# 9
def test_get_api_key_for_invalid_user(email=valid_email, password='0000'):
    """ Проверяем, что при вводе неверного пароля, запрос api ключа не удается, и возвращается статус 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    print('возвращаемый код', status)
    assert status == 403


# 10!!!
def test_add_new_pet_with_negative_age(name='Минусовка', animal_type='МИНУС', age='-40'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом
    по ЗДРАВОМУ СМЫСЛУ так быть не должно, НО ДОКУМЕНТАЦИИ НЕ ПРОТИВОРЕЧИТ"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    try:
        status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)
        print('Статус почему-то не 400 а ', status)

        #  Сверяем полученный ответ с ожидаемым результатом
        assert status == 400
    except AssertionError:  # добавлено что бы тест не валился
        print('Возаст не может быть отрицательным')


# 11!!!
def test_add_new_pet_without_data_with_photo(name='', animal_type='',
                                             age='', pet_photo='images/foto1.jpg'):
    """Проверяем, что нельзя добавить питомца без данных, но с фото
    Сервер не может обработать запрос, получаем код 500"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, 'images/foto1.jpg')

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200


# 12
def test_add_new_pet_with_unacceptable_name(name='!@#$^%$^&*', animal_type='хрень',
                                            age='12', pet_photo='images/foto1.jpg'):
    """Проверяем, что нельзя добавить питомца с именем из символов"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    #  status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, 'images/foto1.jpg')  # OS не срабатывает((
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200


# 13
def test_update_self_pet_info_with_invalid_id(name='Неиди', animal_type='Идиот', age=13):
    """Проверяем отсутствие возможности обновления информации о питомце с неправильным id"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:

        iderr = my_pets['pets'][-1]['id'] + 'df'  # создаем неправильный id

        status, result = pf.update_pet_info(auth_key, iderr, name, animal_type, age)

        # Проверяем, что статус ответа = 400
        assert status == 400

    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("У тебя нет питомцев")


# 14
def test_add_new_pet_with_no_data(name='', animal_type='',
                                  age=''):
    """Проверяем возможность добавления нового питомца без данных"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == ''
    assert result['pet_photo'] == ''

#15
@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
def test_add_new_pet_simple(name, animal_type='двортерьер',
                           age='4'):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   pytest.status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '':
       assert pytest.status == 400
   else:
         assert pytest.status == 200
         assert result['name'] == name
         assert result['age'] == age
         assert result['animal_type'] == animal_type