print(f"""# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Е
# сли число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует
#
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19""")

list = [1.1, 1.2, 3.1, 5, 10.01]


def round_numbers(list):
    print(list)
    list2 = []
    list3 = []
    for i in list:
        if "." not in str(i):
            pass
        else:
            list2.append(i)

    for i in list2:
        ii = str(i).split(".")
        list3.append(float("1." + ii[-1]))
    i = max(list3) - min(list3)
    print(round(i, 3))


round_numbers(list)
