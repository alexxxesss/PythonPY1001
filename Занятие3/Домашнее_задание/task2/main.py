def check_string(str_):
    base = set('01')

    for d in set(str_):  # выделяем все уникальные символы из строки
        if d not in base:
            return "Строка не является двоичным числом"
    print("-----")
    return "Строка является двоичным числом"


if __name__ == "__main__":

    str_input = input('Введите строку, которую хотите проверить на двоичное число: ')
    print(check_string(str_input))
