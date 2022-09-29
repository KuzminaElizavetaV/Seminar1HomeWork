# Задача 5 VERY HARD SORT необязательная
#
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры.
# Отсортировать элементы по возрастанию слева направо и сверху вниз.
#
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
#
# После сортировки
# 1 2 3 4
# 5 7 9 10
import random
line = int(input('Введите количество срок двумерного масссива: '))
column = int(input('Введите количество столбцов двумерного масссива: '))
matrix_sort = []
list = []
matrix = [[random.randint(10, 20) for _ in range(line)] for _ in range(column)] #создаем двумерный массив
print(matrix)
list = sum(matrix, []) # из двумерного массива делаем одномерный
print(list)
for i in range(len(list)): # тут пробегаемся по одномерному массиву и сравниваем 2 соседних элемента, находим наибольшее и меняем местами
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
           list[i], list[j] = list[j], list[i]
print(list)
matrix_sort = [list[i:i + line] for i in range(0, len(list), line)] # из отсортированного одномерного массива преобразуем снова в двумерный той же размерности
print(matrix_sort)
for r in matrix_sort: # Форматированный вывод двумерного массива ввиде таблички
    for x in r:
        print(x, end = '|')
    print()