import sys

data = " (4*3)+(2/2)"

data = data.strip()
data_temp = ""
array_right = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "+", "-", "/", "*"]
for i in data:
    if i in array_right:
        data_temp += i
data = data_temp.replace("+", " + ").replace("-", " - ").replace("/", " / ")\
    .replace("*", " * ").replace("(", " ( ").replace(")", " ) ").strip().split()
if data[0] == array_right[-3] or data[0] == array_right[-4]:
    data.pop(0)
if data[-1] == array_right[-3] or data[0] == array_right[-4]:
    data.pop(-1)

skobka_start = ""
skobka_stop = ""
stop = 0
#пример пока для работы с простыми скобками, потом попробую доделать со сложными через []

print(data)
data = [float(x) if x.isdigit() else x for x in data]
print(data)

while len(data) > 1:
    if (str(skobka_start).isdigit() and str(skobka_stop).isdigit()):
        for i in range(skobka_start, skobka_stop):
            if data[i] == "*" or data[i] == "/":
                if data[i] == "*":
                    data[i-1] = data[i-1] * data[i+1]
                    data[i] = "D"
                    data[i+1] = "D"
                if data[i] == "/":
                    data[i-1] = data[i-1] / data[i+1]
                    data[i] = "D"
                    data[i+1] = "D"
            if data[i] == "+" or data[i] == "-":
                if data[i] == "+":
                    data[i-1] = data[i-1] + data[i+1]
                    data[i] = "D"
                    data[i+1] = "D"
                if data[i] == "-":
                    data[i-1] = data[i-1] - data[i+1]
                    data[i] = "D"
                    data[i+1] = "D"
        data.remove("(")
        data.remove(")")
        data = [x for x in data if x != "D"]
        skobka_start, skobka_stop = "", ""
        print(data)
        stop = 0

    for i in range(0, len(data)):
        if data[i] == "(":
            skobka_start = i
        if data[i] == ")":
            skobka_stop = i
            stop = 1
            break


    if stop != 1:
            for i in range(len(data)):
                if data[i] == "*" or data[i] == "/":
                    if data[i] == "*":
                        data[i - 1] = data[i - 1] * data[i + 1]
                        data[i] = "D"
                        data[i + 1] = "D"
                    if data[i] == "/":
                        data[i - 1] = data[i - 1] / data[i + 1]
                        data[i] = "D"
                        data[i + 1] = "D"
                if data[i] == "+" or data[i] == "-":
                    if data[i] == "+":
                        data[i - 1] = data[i - 1] + data[i + 1]
                        data[i] = "D"
                        data[i + 1] = "D"
                    if data[i] == "-":
                        data[i - 1] = data[i - 1] - data[i + 1]
                        data[i] = "D"
                        data[i + 1] = "D"
            data = [x for x in data if x != "D"]

print(data)