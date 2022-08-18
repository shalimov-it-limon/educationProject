while True:
    try:
        ticket = abs(int(input('Введите, пожалуйста, желаемое количество билетов: ')))
        break
    except ValueError:
        print('Введите, пожалуйста, целое число.')
        exit()

while True:
    try:
        age = input('Введите, пожалуйста, через запятую возраст посетителей\n'
                    '(количество полных лет): ').split(',')
        N_age = sorted(list(map(int, age)))
        break
    except ValueError:
        print('Введите, пожалуйста, возраст числами и через запятую.')
        exit()

for i in N_age:
    if i < 18:
        children = i
        print(f'Для посетителя {children} лет билет предоставлен бесплатно.')
    elif 18 <= i < 25:
        youth = i
        prise1 = 990
        print(f'Для посетителя {youth} лет стоимость билета составит {prise1} рублей.')
    elif 25 <= i:
        adult = i
        prise2 = 1390
        print(f'Для посетителя {adult} лет стоимость билета составит {prise2} рублей.')
else:
    print('-' * 20)
summ = 0
for i in N_age:
    if 18 <= i < 25:
        summ += 990
    elif 25 <= i:
        summ += 1390
        print('Сумма к оплате составит: ', summ)
else:
    print('Добро пожаловать на конференцию')
if ticket > 3:
    summ *= 0.9
    print('Сумма к оплате со скидкой составит: ', summ)
else:
    print()









# len(list(ticket)) == len(list(N_age))
# while True:
#     try:
#         age = input('Введите, пожалуста, через запятую возраст посетителей\n'
#                     '(количество полных лет): ').split(',')
#         N_age = sorted(list(map(int, age)))
#         for i in N_age:
#             if i > 115 or i <= 0:
#                 print('Вы либо слишком стары, либо еще не родились.')
#             break
#     except ValueError:
#                 print('Вы либо слишком стары, либо еще не родились.')


# print('значение' if a % 3 == 1 else 'Значение 2')