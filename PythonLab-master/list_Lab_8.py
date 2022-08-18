ann = ['west', 'east', 'south', 'north', 'world', 'earth', 'peace']
# print(ann)
# i - любое числовое значение.
ann.append('sky') # Добавляет только один аргумент. Добавить.
print(ann)
ann_Q = ['quarc', 'quantum']
print(ann_Q)
print('-' * 20)

ann.extend(ann_Q) # Второй список добавился в конец 1-го. Расширить.
print(ann)
print('-' * 20)

ann.insert(4, 'mouth') # Вставляет после числа-номера элемента (i) новое значение. Вставка, вклейка.
print(ann)
# ann.insert() Обязательно 2 элемента. И только по одной штуке за раз.
print('-' * 20)

ann.remove('mouth') # Удалять элемент.
print(ann)
ann.insert(4, 'mouth')
ann.insert(5, 'роза')
ann.insert(7, 'профи')
print(ann)
print('-' * 20)

# ann.pop([i])