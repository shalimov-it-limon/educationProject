G = {"Адмиралтейская" :
         {"Садовая" : 4},
     "Садовая" :
         {"Сенная площадь" : 3,
          "Спасская" : 3,
          "Адмиралтейская" : 4,
          "Звенигородская" : 5},
     "Сенная площадь" :
         {"Садовая" : 3,
          "Спасская" : 3},
     "Спасская" :
         {"Садовая" : 3,
          "Сенная площадь" : 3,
          "Достоевская" : 4},
     "Звенигородская" :
         {"Пушкинская" : 3,
          "Садовая" : 5},
     "Пушкинская" :
         {"Звенигородская" : 3,
          "Владимирская" : 4},
     "Владимирская" :
         {"Достоевская" : 3,
          "Пушкинская" : 4},
     "Достоевская" :
         {"Владимирская" : 3,
          "Спасская" : 4}}

D = {k : 100 for k in G.keys()} # расстояния
start_k = 'Адмиралтейская' # стартовая вершина
D[start_k] = 0 # расстояние от неё до самой себя равно нулю
U = {k : False for k in G.keys()} # флаги просмотра вершин
P = {k : None for k in G.keys()}

for _ in range(len(D)):
    # выбираем среди непросмотренных наименьшее по расстоянию
    min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])

    for v in G[min_k].keys(): # проходимся по всем смежным вершинам
        D[v] = min(D[v], D[min_k] + G[min_k][v]) # минимум
    U[min_k] = True # просмотренную вершину помечаем

print(D)
pointer = "Адмиралтейская" # куда должны прийти
while pointer is not None: # перемещаемся, пока не придём в стартовую точку
    print(pointer)
    pointer = P[pointer]


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
# создали класс узла, а в конструкторе записали значение, которое должно храниться в нём.
# Также инициализировали левого и правого потомка. Пока что в них ничего не хранится —
# нужно иметь процедуру вставки новых элементов.

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self
# Если в текущем узле нет левого потомка, то новый узел вставляем на его место.
# Если левый потомок уже существует — он становится таким же левым потомком, но уже нового узла.
# Иными словами, он остается левым, но его глубина увеличивается. Аналогично поступим с правым.

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

# Рассмотрим префиксный подход. Сначала мы должны обработать значение самого узла
# (поэтому он и префиксный), а затем рекурсивно проделать то же самое с левым потомком,
# и затем — с правым. В качестве процедуры обработки узла возьмём самое простое — печать его значения.


def pre_order(self):
    print(self.value) # процедура обработки

    if self.left_child is not None: # если левый потомок существует
        self.left_child.pre_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.pre_order() # рекурсивно вызываем функцию


# node_root.pre_order()

# постфиксного обхода в глубину.


def post_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.post_order() # рекурсивно вызываем функцию

    if self.right_child is not None: # если правый потомок существует
        self.right_child.post_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

# Инфиксный подход заключается в том, что порядок обработки узла и его потомков смешивается:
# сначала шагаем в левое поддерево, потом обрабатываем сам узел, затем — правое поддерево.
# В итоге получается, что мы как будто «читаем» дерево слева направо.

# Метод инфиксного обхода в глубину:

def in_order(self):
    if self.left_child is not None: # если левый потомок существует
        self.left_child.in_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

    if self.right_child is not None: # если правый потомок существует
        self.right_child.in_order() # рекурсивно вызываем функцию

# В результате инфиксного обхода получаем следующий порядок узлов.

node_root.in_order()