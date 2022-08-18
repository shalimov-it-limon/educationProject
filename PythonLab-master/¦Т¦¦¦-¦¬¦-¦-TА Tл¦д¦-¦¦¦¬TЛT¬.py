f = open('Частушка.txt') # Открыть для чтения.
print(f.read())
f.close()
f = open('Частушка.txt', 'w') # Открыть для чтения и записи. Перезапись. Старое не остается.
f.write('Все татары кроме Я, все в кусты, а я в трава!') # Перезапись в файл.
f.close()
f = open('Частушка.txt', 'rt') # Открыть для чтения именно ТЕКСТОВЫЙ файл.
print(f.read())
f.close()
f = open('Частушка.txt', 'a') # Открыть для чтения и дозаписи. Старое остается.
f.write('Горшок, тебя я с детства помню!') # Перезапись в файл.
f.close()
f = open('Частушка.txt', 'rt') # Открыть для чтения именно ТЕКСТОВЫЙ файл.
print(f.read())
f.close()
f = open('Частушка.txt', 'a') # Открыть для чтения и дозаписи. Старое остается.
f.write('\nТы был в цветочках и стальной!') # Перезапись в файл.
f.close()
f = open('Частушка.txt', 'rt') # Открыть для чтения именно ТЕКСТОВЫЙ файл.
print(f.read(25))
f.close()


f = '''Все татары кроме Я, все в кусты, а я в трава!Горшок, тебя я с детства помню!
Ты был в цветочках и стальной!'''


def more_a(a):
    count = {}
    for char in f:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

item = str('а')
print(more_a(item))

f = open('Частушка.txt', 'rt') # Открыть для чтения именно ТЕКСТОВЫЙ файл.
print(f.readline()) # Читает одну строку.
f.close()

f = open('Частушка.txt', 'rt')
for i in f.readlines():  # Читает все строки.
    print(i)
f.close()

f = open('track.txt', 'w')
f.write('И вот тут я что-то из Шарма написала.')
f.close()

f = open('track.txt')
print(f.read())

f = open('track.txt', 'a')
f.write('Создала из Шарма и дописала из Шарма. Люблю Шарм.')
f.close()

f = open('track.txt')
print(f.read())

# 'rb' - чтение бинарных файлов.

f = open('track.txt', 'rt')
for i in f: # Цикл построчно проходит под доку и выводит поочередно строчки, как и readlines.
    print(i)
f.close()

with open('track.txt', 'rt') as f:
    for i in f:
        print(i)
f.close()
f = open('track.txt', 'r')
print(f.read(14))
f.close()

# ШИФРОВАНИЕ

a = 'абвгдежзик' # Шифровщик
b = 'АБВГДИЕЖЗИК' # Дешифрощик

f = open('track.txt', 'r') # Открываю свой файл, читаю.
text = f.read()  # Сохраняю его в переменной.
f.close()

newtext = ''  # Переменная, куда сохранится дешифрованный текст.

for i in text:   # Для символа в тексте.
    for j in range(len(a)):  # Для символа в строке шифратора надо знать индекс.
        if i == a[j]: # Если в шифраторе есть символ.
            i = b[j]  # То символ становится символом из дешифратора.
        newtext += i

f = open('track_shif.txt', 'w')  # Создаю новый файл.
f.write(newtext)
f.close()

with open('track_shif.txt')as f:
    print(f.read())
f.close()

## Сколько слов в тексте.

a = 'абвгдежзик' # Шифровщик
b = 'АБВГДИЕЖЗИК' # Дешифрощик

f = open('track.txt', 'r') # Открываю свой файл, читаю.
text = f.readlines()  # Сохраняю его в переменной.
f.close()

count = 0  # Переменная-счетчик для слов.
for i in text: # Берется строка.
    a = i.split() # split разделяет строку на слова в список, ориентируясь по пробелам.
    count += len(a)
    print(count)

f = open('track.txt', 'a') # Открываю свой файл, читаю.
f.write(f'\nВ тексте {count} слов.')
f.close()

with open('track.txt')as f:
    print(f.read())
f.close()