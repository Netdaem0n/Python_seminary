# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "абв привет я абвешка а ты абв"
print(text)

remove_abv_1 = text.replace("абв", "")
remove_abv_2 = text.split()
remove_abv_2 = [i for i in remove_abv_2 if "абв" not in i.lower()]
remove_abv_2 = " ".join(remove_abv_2)
print(f"Вариант 1 - {remove_abv_1} \n"
      f"Вариант 2 - {remove_abv_2}")