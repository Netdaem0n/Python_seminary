import math
import random

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input().strip().strip("-").strip("+").strip(".").strip(",")
print(sum([int(i) for i in number]))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input())
list_new = []
for i in range(1, number+1):
    print(i)
    list_new.append(math.factorial(i))
print(list_new)

# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности
# (для проверки сумма для 4 элементов = 9,06 (примерно))

n = int(input())
p = [(1+1/i)**i for i in range(1, n+1)]
print(p)
print((sum(p)))

# Реализуйте алгоритм перемешивания списка, без использования встроеных методов
# (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random
my_list = [5, 9, 10, 11, 20]
def rand_sh(list):
    buf = 0
    for i in range(len(list)):
        rand_number_index = random.randint(0, len(list)-1)
        buf = list[i]
        list[i] = list[rand_number_index]
        list[rand_number_index] = buf
    return list

print(my_list)
my_list = rand_sh(my_list)
print(my_list)
