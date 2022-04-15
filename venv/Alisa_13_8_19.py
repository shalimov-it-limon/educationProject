# ввод количества билетов
n_tiket=abs(int(input('Введите количество посетителей = ')))

# ввод списка возрастов
L_age = list(map(int, input(f'введите возраст посетителей через запятую, всего {n_tiket} билетов = ').split(',')))

# проверка соответствия списка возрастов количеству билетов
if len(L_age)<n_tiket: # если список возрастов меньше количества билетов, то остаток по полному тарифу
    print(f'Билетов заказано {n_tiket} возраст заявлен на {len(L_age)} посетителей,\n остаток: {n_tiket-len(L_age)} по полному тарифу ')
    i=0
    while i<=n_tiket-len(L_age):
        L_age.append(26)
        i+=1
elif len(L_age)>n_tiket: # если список возрастов больше количества билетов, то лишние удаляются с конца списка
    i = 0
    while i < len(L_age)-n_tiket:
        L_age.pop(len(L_age)-1)
        i += 1

print(L_age)

summ=0
for i in L_age:

 if i < 18:
    summ += 0

 elif 18<=i<=25:
    summ += 990

 elif 25<i :
    summ += 1390

 if n_tiket > 3:
     summ *= 0.9
print(summ)