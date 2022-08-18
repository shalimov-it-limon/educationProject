f = open('ЭКспреимент букв.txt', 'w')
f.write('Сшит колпак непокалпаковски. Колпак надо распколпаковать и перевыколпаковать!')
f.close()
f = open('ЭКспреимент букв.txt', 'rt')
text = f.readlines()
f.close()
count = 0
for i in text:
    a = i.split()  # split разделяет строку на слова в список, ориентируясь по пробелам.
    # b = a.split()
    count += len(a)
    print(count)
count = f'\nВ тексте {count} слов.'
f = open('ЭКспреимент букв.txt', 'a')
f.write(count)
f.close()

f = open('ЭКспреимент букв.txt', 'rt')
print(f.read())
f.close()