# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd
file_name_in = "in.txt"
file_name_out = "out.txt"


def open_file(file):
    with open(file, "r") as f:
        file_data = f.read()
    return file_data

def write_file(file, data):
    with open(file, "w") as f:
        f.write(data)



def compress(my_string: str) -> str:
    counter = 1
    result = ""
    curr = ""
    for i in range(1, len(my_string)):
        prev = my_string[i - 1]
        curr = my_string[i]

        if prev == curr:
            counter += 1
        elif prev != curr:
            result += f'{counter}{prev}'
            counter = 1

    result += f'{counter}{curr}'
    return result


def decompress(some_string: str) -> str:
    result = ""
    num = ""

    for c in some_string:
        if ord('0') <= ord(c) <= ord('9'):
            num += c
        else:
            result += c * int(num)
            num = ""

    return result

print(compress("aaaaaaabbbbbbcccccccccd"))
print(decompress("7a6b9c1d"))

write_file(file_name_out, compress(open_file(file_name_in)))
