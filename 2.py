print(f"""# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.""")


my_list1 = [11, 3, 6, 110, 20, 19, 33, 4, 11, 15]
my_list2 = [11, 3, 6, 5, 3]


def remove_it(my_list):
    if len(my_list) % 2 == 0:
        list2 = [my_list[i] * my_list[-1 - i] for i in range(0, int(len(my_list)/2))]
        print(f"Результат (список четный) - {list2}")
    if len(my_list) % 2 != 0:
        pop_obj = len(my_list) // 2
        print("Лишний элемент (индекс)- ", pop_obj)
        my_list.pop(pop_obj)
        list2 = [my_list[i] * my_list[-1 - i] for i in range(0, int(len(my_list)/2))]
        print(f"Результат (список нечетный) - {list2}")


remove_it(my_list1)
remove_it(my_list2)
