#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

i = 100

def chislo_to_sistema(chislo, sistema):
      string_new = ""
      while chislo != 0:
            string_new += str(chislo % sistema)
            chislo = chislo // sistema
      return string_new[::-1]

print(chislo_to_sistema(100, 2))
