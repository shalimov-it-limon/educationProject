# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
#  для работы над матрицами нам нужны два цикла, где один вложен в другой.
#  Для того, чтобы обойти всю таблицу, нужен цикл, который будет последовательно
#  перебирать все строки, а также цикл, который будет перебирать все столбцы для каждой строки.
#  То есть обход матрицы будет слева-направо, сверху-вниз.
# # Обычно индекс, который отвечает за строки обозначают как i, а индекс, отвечающий за столбцы — j,

# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# # 0 1 2 3 4 5
# for i in range(N):
#     for j in range(M):
#         print(matrix[i][j], end=" ")
#     print()  # перенос на новую строку


# Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки, а также их индексы.
# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]

# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
# for row in random_matrix:  # здесь мы целиком берем каждую строку
#    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#    max_index = 0
#    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#    max_value = row[max_index]  # для максимального значения тоже самое
#
#   for index_col in range(len(row)):
#        if value < min_value:
#            min_value = value
#            min_index = index_col
#        if value > max_value:
#            max_value = value
#            max_index = index_col
#    min_value_rows.append(min_value)
#    min_index_rows.append(min_index)
#    max_value_rows.append(max_value)
#    max_index_rows.append(max_index)

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

for row in random_matrix:  # здесь мы целиком берем каждую сроку
    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
    max_index = 0
    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
    max_value = row[max_index]  # для максимального значения тоже самое
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print(min_value_rows)
print(min_index_rows)
print(max_value_rows)
print(max_index_rows)