import os

sayt = input()

if 'https://' in sayt:  # in проверяет наличие в переменной указанного после if набора символов.
    os.system('start' + sayt)
    print('if')
elif 'www.' in sayt:
    sayt = 'https://' + sayt
    os.system('start' + sayt)
    print('elif')
else:
    sayt = 'https://www.' + sayt
    os.system('start' + sayt)
    print('else')