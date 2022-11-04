# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11
def remove_any(data):
    data = str(data)
    return list(data.strip().strip("-").strip("+"))

chislo = "-+0.,6782"

chislo = remove_any(chislo)
chislo_new = list(map(lambda x: x.replace(".", "0").replace(",", "0"), chislo))
chislo_new = list(map(lambda x: int(x), chislo_new))
print(chislo)
print(sum(chislo_new))
