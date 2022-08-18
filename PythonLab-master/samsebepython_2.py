import operator
print('Other VAR')
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Сортируем в порядке возрастания:

result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)

# И в порядке убывания:
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print(result)

# Напишите программу для слияния нескольких словарей в один.
print('Other VAR')
a = {'b':'1', 'c':'2', 'd':'3', 'f':'4'}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

result = {}
for b in (a, d):
    result.update(b)
print(result)

# А можно с помощью «звёздочного» синтаксиса:

result = {**a, **b}
print(result)


# Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# Можно воспользоваться функцией sorted:
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)

# Аналогичный результат можно получить с помощью функции nlargest из модуля heapq:

from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)
print(result)
