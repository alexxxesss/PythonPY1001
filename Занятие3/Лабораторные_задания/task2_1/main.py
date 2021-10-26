def task(str1, str2, k):
    if str1[:k] == str2[:k]:
        print("ДА")
    else:
        print("НЕТ")


if __name__ == "__main__":

    str_1 = input('Введите первую строку: ')
    str_2 = input('Введите вторую строку: ')
    number = int(input('Введите k первых символов, которые нужно проверить: '))

    task(str_1, str_2, number)
