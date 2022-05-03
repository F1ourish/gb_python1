# I. Реализовать следующие функции для работы с массивами:

arr = list(map(int, input("Enter your array: ").split(" ")))


# print("\nEntered array: ", end=' ')
# for i in range(len(arr)):
#     print(arr[i], end=' ')


# 1. Поиск минимума

def min_array(a):
    return min(a)


# 2. Поиск максимума

def max_array(a):
    return max(a)


# 3. Поиск суммы элементов массива

def sum_array(*args):
    return sum(*args)
    # return sum((int(arr[i]) for i in range(0, int(len(arr)))))


# 4. Поиск произведения элементов массива

def multiplicate_array(a):
    result = 1
    for i in range(len(a)):
        result *= a[i]
    return result


# 5. Поиск индекса заданного элемента в массиве, если такого элемента в массиве нет то возвращать -1

def index_search(a):
    for i in range(len(arr)):
        if a == arr[i]:
            return i
    return -1


# 6. Проверка наличия элемента в массиве. Возвращает true, если элемент в массиве есть, false – нет.

def el_search(a):
    for i in range(len(arr)):
        if a == arr[i]:
            return True
    return False


# 7. Печать массива на экран

def print_array():
    print('\nThe array is: ', end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')


# 8. Среднее арифметическое элеметов массива

def average(*args):
    return int(sum(*args) / 2)


# 9. Подсчёт количества отрицательных элементов массива

def neg_el_count():
    count = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            count += 1
    return count


# 10. Подсчёт количества вхождений элемента в массив

def el_count(b):
    count = 0
    for i in range(len(arr)):
        if arr[i] == b:
            count += 1
    return count


# 11. Подсчёт количества чётных элементов в массиве

def even_el_count():
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count += 1
    return count


# 12. Подсчёт количества положительных элементов в массиве

def pos_el_count():
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    return count


# 13. Подсчёт количества нечётных элементов в массиве

def odd_el_count():
    count = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            count += 1
    return count


# 14. Проверка является ли массив отсортированным по возрастанию. Если массив отсортирован, то возвращать true, иначе - false.

def sorted_or_not():
    c = arr[0]
    for i in range(len(arr)):
        if arr[i] >= c:
            c = arr[i]
        else:
            return False
    return True


# II. Реализовать следующие функции:
# 1. Функцию, которая вычисляет число a в степени n

def n_degree_of_a(a, b):
    return a ** b


# 2. Функцию, которая вычисляет факториал числа n

def factorial(a):
    count = 1
    result = 1
    if a == 0:
        return 1
    else:
        while count <= a:
            result = result * count
            count += 1
        return result


# 3. Функцию, которая вычисляет сумму цифр произвольного целого числа n

def sum_of_digits(a):
    result = 0
    a = abs(a)
    while a // 10 or a % 10 != 0:
        result = result + (a % 10)
        a = a // 10
    return result


# 4. Функцию, которая проверяет является ли заданное число n полиндромом

# def palindrome(a):
#     digits = len(str(a))
#     c = 1
#     if a // 10 == 0 and a % 10 != 0:
#         return print("It's a palindrome.")
#     else:
#         while c < digits // 2:
#             if a // (10 ** (digits - c)) == a % 10:
#                 a = a // 10 - a // (10 ** (digits - c))
#                 c += 1
#             else:
#                 return print("It's not a palindrome.")
#         return print("it's a palindrome.")


# альтернативный вариант через массив и слайс:

def palindrome1(a):
    a = str(a)
    if a == a[::-1]:
        return print("\nEntered number is a palindrome.")
    else:
        return print("\nEntered number is not a palindrome.")


# 5. Функцию, складывающую два целых числа

def summary(a, b):
    return a + b


# 6. Функцию, определяющую является ли число простым, то есть возвращающую true, если число простое, иначе - false
# воспользуемся перебором делителей (пробным делением)

def prime_num_check(a):
    i = int(a ** 0.5)  # возможные делители
    while i >= 2:
        if a % i == 0:
            return False
        else:
            i -= 1
    return True


# 7. Функцию, определяющую является ли число чётным, то есть возвращающую true, если число чётное, иначе - false

def even_num_check(a):
    if a % 2 == 0:
        return True
    else:
        return False


def main():
    print('\nMinimal element of array is', min_array(arr))
    print('\nMaximal element of array is', max_array(arr))
    print('\nSummary of array is', sum_array(arr))
    print('\nProduct of array numbers is', multiplicate_array(arr))
    print('\nThe index is:', index_search(int(input("\nEnter an element of array: "))))
    print('\nIs number in array?', el_search(int(input("\nEnter a number: "))))
    print_array()
    print('\n\nThe average of array is:', average(arr))
    print('\nThere are', neg_el_count(), 'negative element(s) in array.')
    print('\nThe count of entered elements in array is:', el_count(int(input("\nEnter a number: "))))
    print('\nThere are', even_el_count(), 'even element(s) in array.')
    print('\nThere are', pos_el_count(), 'positive element(s) in array.')
    print('\nIs array sorted?', sorted_or_not())
    a = int(input("\nEnter a number: "))
    n = int(input("\nEnter a degree: "))
    print("\n", a, "in degree of", n, "is", n_degree_of_a(a, n))
    a = int(input("\nEnter factorial number: "))
    print("\nThe factorial of", a, "is", factorial(a))
    print("\nThe sum of digits of entered number is", sum_of_digits(int(input("\nEnter any integer number for it's summary of digits: "))))
    palindrome1(abs(int(input("\nEnter any integer number for palindrome check: "))))
    a = int(input("\nEnter first number: "))
    b = int(input("\nEnter second number: "))
    print("\nSummary of entered numbers is:", summary(a, b))
    print("\nIs entered number prime?", prime_num_check(int(input("\nEnter any integer number greater than 1: "))))
    print("\nIs entered number even?", even_num_check(int(input("\nEnter any integer number: "))))


main()
