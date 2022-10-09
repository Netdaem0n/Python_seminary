print(f"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.""")

n = int(input("Введите N: "))

list = []
i = 2

while n != 0 :
    if n >=0 and n <= 9:
        list.append(n)
        break
    if n % i == 0:
        list.append(i)
        n = n // i
        i = 2
    else:
        i += 1

print(list)

