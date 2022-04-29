# -*- coding: cp1251 -*-

alpha = '�������������������������������'
alphaUp = '�����Ũ�������������������������'
number = int(input('������� �����, �� ������� ����� �������� �����: '))

summary = ''

def changChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return  char

#���� text.txt ������ ������ � ��� �� �����, ��� ����� ������ ������ � ������ ��������� �����-�� �����
with open('text.txt',encoding='cp1251') as myFile:
    for line in myFile:
        for char in line:
            summary += changChar(char)

#���� output.txt ������ ������ � ��� �� �����, ��� ����� ������ ������
with open('output.txt','w',encoding='cp1251') as myFile:
    myFile.write(summary)