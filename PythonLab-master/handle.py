# Открывается файл для чтения только в той папке, которая прописана к консоли или  Шарме.
# handle = open("pup.txt")
# handle = open(r"D:\Общие документы\AnnCherdan\Pup.txt", "r")
# "r" показывает, что строка обрабатывается, как исходная.
# print('D:\Общие документы\AnnCherdan\Python')
handle = open("pup.txt", "r")
data = handle.read()
print(data)
handle.close()
print('-' * 20)

handle = open("pup.txt", "r")
data = handle.readline(35) # Читает только первую строку. В скобках можно указать количество симолов к возвоату
print(data)
handle.close()
print('-' * 20)

handle = open("pup.txt", "r")
data = handle.readlines() # Считывает все линии в виде списка методом readlines().
print(data)
handle.close()