import numpy as np
# Решите без использования циклов средставми NumPy (каждый пункт решается в 1-2 строчки)
#
# Создайте вектор с элементами от 12 до 42
# Создайте вектор из нулей длины 12, но его пятый елемент должен быть равен 1
# Создайте матрицу (3, 3), заполненую от 0 до 8
# Найдите все положительные числа в np.array([1,2,0,0,4,0])
# Умножьте матрицу размерности (5, 3) на (3, 2)
# Создайте матрицу (10, 10) так, чтобы на границе были 0, а внтури 1
# Создайте рандомный вектор и отсортируйте его
# Каков эквивалент функции enumerate для numpy массивов?


v1 = np.arange(12, 43)
print(v1)
print()

v2 = np.zeros(12)
v2[4]=1
print(v2)
print()

v3 = np.arange(9).reshape((3, 3))
print(v3)
print()

v4 = np.array([1,2,0,0,4,0])
print(v4[v4 > 0])
print()

v5 = np.random.random((5, 3)).dot(np.random.random((3, 2)))
print(v5)
print()

v6 = np.hstack((np.zeros((10, 1)), np.vstack((np.zeros((1, 8)), np.ones((8, 8)), np.zeros((1, 8)))), np.zeros((10, 1))))
print(v6)
print()

v7 = np.random.random(10)
print('Оригинальный массив:\n', v7)
print('Отсортированный массив:\n', np.sort(v7))
print()

print('Эквивалентом функции enumerate для numpy массивов является numpy.ndenumerate')
print()


