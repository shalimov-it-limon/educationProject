# -*- coding: cp1251 -*-

alpha = 'абвгдеЁжзиклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''

def changChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return  char

#Файл text.txt должен лежать в той же папке, где лежит данный скрипт и должен содержать какой-то текст
with open('text.txt',encoding='cp1251') as myFile:
    for line in myFile:
        for char in line:
            summary += changChar(char)

#Файл output.txt должен лежать в той же папке, где лежит данный скрипт
with open('output.txt','w',encoding='cp1251') as myFile:
    myFile.write(summary)