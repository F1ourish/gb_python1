# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

lst = []
while True:
    string = input("Enter text: ")
    if string == '':
        exit()
    else:
        next_string = string + '\n'
        lst.append(next_string)

    with open("text1.txt", "w") as f_obj:
        f_obj.writelines(lst)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("text2.txt") as f_obj:
    strings = 0
    letters = 0
    count = 0
    for string in f_obj:
        strings += string.count("\n")
        letters = len(string) - 1
        count += 1
        print(letters, "letters in", count, "string")
    print("\nTotal strings count is", strings)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

sal_sum = 0
count = 0
employees = []
with open("text3.txt", "r") as f_obj:
    for line in f_obj:
        # print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            employees.append(tokens[0])
        sal_sum += int(tokens[1])
        count += 1
av_sal = sal_sum / count


def print_emp():
    emp_name = ''
    for i in range(len(employees)):
        if i == len(employees) - 1:
            emp_name += str(employees[i]) + '.'
        else:
            emp_name += str(employees[i]) + ', '
    return emp_name


print("\nEmployees with salary lower then 20 000:", print_emp())
print("Average salary of all employees is:", int(av_sal))

# 4. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open("text4.txt", "w+") as f_obj:
        line = input("Enter numbers using 'Space' as a spliter.\n")
        f_obj.writelines(line)
        nums = line.split()

        print("\nSummary of entered numbers =", sum(map(int, nums)))
except IOError:
    print("Input-output error!")
except ValueError:
    print("Input-output error!")
