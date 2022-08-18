# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)

# d = {2: 'два', 3: 'три'}
# d[4] = "четыре"
# print(d)
# for key in d.keys():
#     print(key)
#
# for value in d.values():
#     print(value)
#
# for key, value in d.items(): # items возвращает кортеж из ключей и значений.
#     print(key, value)
#
# ticket = int(input('Введите, пожалуста, необходимое количество билетов: ')) # клиент вводит количество билетов.
# age = int(input('Введите, пожалуста, через запятую, возраст посетителей\n'
#             '(количество полных лет): ')).split(',') # клиет вводит возраст посетителей.
# # ticket = list(map(int, ticket))
# # age = list(map(int, age))
# # print(age)
# child = 0 < 18 # определен возраст детей.
# youth = 18 <= {age} < 25 # определен возраст подростков.
# adult = 25 <= {age} # определен возраст взрослых.
# for i in child:
# if age in child:
#     print('Free')
# elif age in youth:
#     print('990')
# elif age in adult:
#     print('1390')
while True:
    try:
        age = input('Введите, пожалуста, через запятую возраст посетителей\n'
                    '(количество полных лет): ').split(',')
        N_age = sorted(list(map(int, age)))
        for i in N_age:
            if i > 115 or i <= 0:
                print('Вы либо слишком стары, либо еще не родились.')
            break
    except ValueError:
                print('Вы либо слишком стары, либо еще не родились.')

