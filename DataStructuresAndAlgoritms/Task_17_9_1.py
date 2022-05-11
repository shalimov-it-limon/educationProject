import scripts

my_numbers = map(int, input('Введите числа через пробел:').split(' '))
selected_number = int(input('Задайте любое число: '))
# Преобразование введёной последовательности в список
my_list = list(my_numbers)
my_list.append(selected_number)
# Сортировка списка по возрастанию элементов в нем (сортировка слиянием)
sorted_list = scripts.merge_sort(my_list)

if selected_number < sorted_list[0]:
    print("Все числа из последовательности больше заданного числа")
elif selected_number > sorted_list[-1]:
    print("Все числа из последовательности меньше заданного числа")
else:
    position = scripts.binary_search(sorted_list,selected_number,0,len(sorted_list))
    print("Искомый номер позиции равен ",position-1)
