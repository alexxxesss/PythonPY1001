def func_n(n):
    list_n = [int(i) for i in str(n)]

    if 4 and 8 in set(list_n) or 9 in set(list_n):
        return "Условие выполняется"
    else:
        return "Условие НЕ выполняется"

    # for i in list_n:
    #     if (i == 4 and i == 8) or i == 9 in list_n:
    #         return 'Цифры 4 и 8 или фифра 9 входят в вводимое число'
    #     else:
    #         return 'Условие задания не выполняется'


if __name__ == "__main__":
    N = int(input('Введите двухзначное число: '))
    print(func_n(N))
