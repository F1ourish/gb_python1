import random as rd

# 15. Задать массив из 8 элементов и вывести их на экран

# arr = []
# print("Введите 8 элементов массива.")
# for i in range(8):
#     print(i+1, " элемент:", end=' ')
#     el = int(input())
#     arr.append(el)
# c = 0
# print("Получился следующий массив:")
# while c < 8:
#     print(arr[c], end=' ')
#     c += 1

# 16. Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран

# arr = []
# for i in range(8):
#     el = rd.randint(0, 1)
#     arr.append(el)
# c = 0
# while c < 8:
#     print(arr[c], end=' ')
#     c += 1

# 17. Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

# arr = []
# for i in range(12):
#     el = rd.randint(0, 9)
#     arr.append(el)
# print("Заданный массив чисел: ", list(i for i in arr))
# print("\nСумма отрицательных чисел массива равна: ", sum(i for i in arr if i < 0))
# print("\nСумма положительных чисел массива равна: ", sum(i for i in arr if i > 0))

# 18. Написать программу замену элементов массива на противоположные

# arr = []
# arr_len = int(input("Введите число элементов массива: "))
# for i in range(arr_len):
#     el = rd.randint(-10, 10)
#     arr.append(el)
#
# reverse_arr = list(map(lambda x: x * -1, arr))
# print("\nЗаданный массив: ", arr)
# print("\nМассив с противоположными знаками: ", reverse_arr)

# 19. Определить, присутствует ли в заданном массиве, некоторое число

# arr = []
# arr_len = int(input("Введите число элементов массива: "))
# for i in range(arr_len):
#     el = rd.randint(0, 10)
#     arr.append(el)
# print("\nЗаданный массив: ", arr)
#
# num = int(input("\nВведите число, для проверки его наличия в массивее: "))
# count = 0
# for i in arr:
#     if i == num:
#        count += 1
# if count > 0:
#     print("\nВведённое число присутствует в заданном массиве.")
# else: print("\nВведённое число отсутствует в заданном массиве.")

# 20. Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

# arr = []
# arr_len = int(input("Введите число элементов массива: "))
# for i in range(arr_len):
#     el = rd.randint(100, 999)
#     arr.append(el)
# print("\nЗаданный массив: ", arr)
# even_count = 0
# odd_count = 0
# for i in arr:
#     if i % 2 == 0:
#        even_count += 1
#     else: odd_count += 1
# print("\nКолличество чётных чисел в заданном массиве равно: ", even_count, " , нечётных: ", odd_count)

# 21. В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

# arr = []
# count = 0
# for i in range(123):
#     el = rd.randint(0, 100)
#     arr.append(el)
# print("\nЗаданный массив: ", arr)
# for i in arr:
#     if i >= 10 and i <= 99:
#         count += 1
# print("\nКоличество элементов массива, принадлежащих отрезку [10, 99] равно: ", count)

# 22. Найти сумму чисел одномерного массива стоящих на нечетной позиции

# arr = []
# arr_len = int(input("Введите число элементов массива: "))
# count = 0
# sum = 0
# for i in range(arr_len):
#     el = rd.randint(0, 100)
#     arr.append(el)
# print("\nЗаданный массив: ", arr)
# for i in arr:
#     if count % 2 != 0:
#         sum = sum + i
#         count += 1
#     else: count += 1
# print("\nСумма чисел массива, стоящих на нечётной позиции равна: ", sum)

# 23. Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# arr = []
# new_arr = []
# arr_len = int(input("Введите чётное число элементов массива: "))
# for i in range(arr_len):
#     el = rd.randint(0, 10)
#     arr.append(el)
# print("\nЗаданный массив: ", arr)
# i = 1
# while i <= arr_len / 2:
#     el = arr[i - 1] * arr[arr_len - i]
#     new_arr.append(el)
#     i += 1
# print("\nНовый массив полученных пар чисел из заданного массива: ", new_arr)

# 24. В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

arr = []
arr_len = int(input("Введите число элементов массива: "))
for i in range(arr_len):
    el = round(rd.uniform(0, 10), 2)
    arr.append(el)
print("\nЗаданный массив: ", arr)
min = arr[0]
max = arr[0]
for i in arr:
    if i > max:
        max = i
    elif i < min:
        min = i
print("\nРазница между максимальными и минимальным элементами массива равна: ", (max - min))
