import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree



html = requests.get('https://www.python.org/').content # получим html главной странички официального сайта Python

tree = lxml.html.document_fromstring(html)
title = tree.xpath \
    ('/html/head/title/text()') # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.

print(title) # выводим полученный заголовок страницы

import requests # импортируем наш знакомый модуль
import lxml.html
from lxml import etree


html = requests.get('https://www.python.org/blogs/').content # получим html главной странички официального сайта python

# # создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Our Blogs Python.org.html', lxml.html.HTMLParser()) # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall('/html/body/div/div[3]/div/section/div/div[1]/div/ul') # помещаем в аргумент методу findall скопированный xpath

# # создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a') # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text) # из этого тега забираем текст - это и будет нашим названием

# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
#
# <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
#
import lxml.html
#
html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''
#
tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)

import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера

ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием