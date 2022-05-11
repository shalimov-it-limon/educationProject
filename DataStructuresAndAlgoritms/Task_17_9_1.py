def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


my_numbers = map(int, input('Введите числа через пробел:').split(' '))
selected_number = int(input('Задайте любое число: '))
# Преобразование введёной последовательности в список
my_list = list(my_numbers)
# Добавляем элемент в список, чтобы поиск корректно отработал
my_list.append(selected_number)
# Сортировка списка по возрастанию элементов в нем (сортировка слиянием)
sorted_list = merge_sort(my_list)

if selected_number < sorted_list[0]:
    print('Все числа из последовательности больше заданного числа')
elif selected_number > sorted_list[-1]:
    print('Все числа из последовательности меньше заданного числа')
else:
    position = binary_search(sorted_list, selected_number, 0, len(sorted_list))
    print('Искомый номер позиции равен ', position - 1)
