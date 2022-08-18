print('Hello, World')
m = 'hello, world'
print(m.replace('h', 'H'), m.replace('w', 'W'))  # BAD Var
print(m.replace('h', 'H').replace('w', 'W'))


# def change_char(x, y):
#     text = input()
#     if text.type == str


m = 'Hello, World'
n = 'Good morning'
print(m + '\nGood morning')
print(m + ', ' + 'Good morning')
gf = 'kl'
f = 'haha'
print(gf + (f.join(n)))
print(m + n + gf + f)

a = (5 + 6) / 2
print(a)


def plus_char(x, y, m):
    a = (x + y) / m
    return a


print(plus_char(5, 6, 2))

a = 10
b = a
print(b)
print('My Var')  #That's working, but not good.
a = 1
b = 2

a = b
b = 1
print(a, b)
print('Other Var')
a = 3
b = 4
temp = a
a = b
b = temp
print(a, b)

a = {'Ann': 'genius', 'Ksan': 'not genius'}
print(a.keys())
print(a.values())
print(*a, ', '.join(a.values()))
print(', '.join(a.keys()) * 2)

# a = 5
# b = 6
# if bool(a > b):
#     print()


def common(a, b):
    if a < b:
        print('Good')
    elif a > b:
        print('Bad')
    else:
        ...


common(8, 6)
