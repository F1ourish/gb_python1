# 1. По двум заданным числам проверять является ли первое квадратом второго

num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

sqr = num2 ** 2
if sqr == num1:
    print("Первое число - квадрат второго числа.")
else:
    print("Первое число не является квадратом второго.")

# 2. Показать числа от -N до N

n = int(input("Введите целое положительное число N: "))

m = n * -1

while m <= n:
    print(m)
    m += 1

# 3. Показать четные числа от 1 до N

count = 1

while count <= n:
    if count % 2 == 0:
        print(count)
        count += 1
    else: count += 1

# 4. Показать последнюю цифру трёхзначного числа

three_dig_num = int(input("Введите целое трёхзначное число: "))
last_num = abs(three_dig_num % 10)
print("Последняя цифра введённого числа = " + str(last_num))

# 5. Найти третью цифру числа или сообщить, что её нет

num = abs(int(input("Введите число: ")))
if abs(num) < 99:
    print("Введённое число имеет меньше трёх знаков")
else:
    while num > 1000:
        num = num // 10
    num = num % 10
    print("Третья цифра введённого числа: " + str(num))

# 6. Программа проверяет пятизначное число на палиндромом.

five_dig_num = abs(int(input("Введите целое пятизначное число: ")))
if five_dig_num // 10000 != five_dig_num % 10:
    print("Введённое число палиндромом не является.")
else:
    new_num = five_dig_num % 10000 // 10
    if new_num // 100 != new_num % 10:
        print("Введённое число палиндромом не является.")
    else:
        print("Введённое число является палиндромом.")

# 7. Показать таблицу квадратов чисел от 1 до N

n = int(input("Введите целое число N: "))
count = 1
print("\nТаблица квадратов от 1 до " + str(n))
while count <= n:
    print("Квадрат числа: " + str(count) + " = " + str(count ** 2))
    count += 1

# 8. Найти кубы чисел от 1 до N

count = 1
print("\nТаблица кубов от 1 до " + str(n))
while count <= n:
    print("Куб числа: " + str(count) + " = " + str(count ** 2))
    count += 1

# 9. Найти сумму чисел от 1 до А

a = int(input("Введите целое положительное число А: "))
count = 1
sum = 0
while count <= a:
    sum = sum + count
    count += 1
print("Сумма чисел от 1 до " + str(a) + " равна " + str(sum))

# 10. Возведите число А в натуральную степень B используя цикл

a = int(input("Введите целое число А: "))
b = int(input("Введите натуральное число степени В: "))
c = a
count = 1

while count < b:
    c = c * a
    count += 1
print("Число " + str(a) + " в степени " + str(b) + " равно: " + str(c))

# 11. Определить количество цифр в числе

num = int(input("Введите целое число: "))
count = 1
while num // 10 > 0:
    num = num // 10
    count += 1
print("В введённом Вами числе " + str(count) + " цифр.")

# 12. Подсчитать сумму цифр в числе

num = abs(int(input("Введите целое число: ")))
sum = 0
while num // 10 > 0 or num % 10 > 0:
    sum = sum + (num % 10)
    num = num // 10
print("Сумма цифр введённого числа равна " + str(sum))

# 13. Написать программу вычисления произведения чисел от 1 до N

n = int(input("Введите целое положительное число N: "))
count = 1
c = 1
while count <= n:
    c = c * count
    count += 1
print("Произведение чисел от 1 до N равно " + str(c))

# 14. Показать кубы чисел, заканчивающихся на четную цифру

print("Кубы чисел от 1 до N, заканчивающихся на чётную цифру")
while count <= n:
    if count ** 3 % 2 == 0:
        print(count ** 3)
    count += 1
