import math


day_of_weak = input()
print("ДА") if day_of_weak == 6 or day_of_weak == 7 else print("Нет")

x = int(input("X:"))
y = int(input("Y:"))
z = int(input("Z:"))
print(not(x or y or z) == (not x and not y and not z))

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))


if x == 0 or y == 0:
    raise Exception("not 0")
elif x > 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')

a = int(input("Enter number of quarter of axis:  "))

if a == 1: print(" The first axis: x from 0 to + ∞, y from 0 to + ∞")
elif a == 2: print(" The second axis: x from 0 to  - ∞, y from 0  to + ∞ ")
elif a == 3: print(" The third axis: x from 0 to  - ∞, y from 0  to - ∞ ")
elif a == 4: print(" The four axis: x from 0 to  + ∞, y from 0  to - ∞ ")

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = round(math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2), 2)
print(distance)