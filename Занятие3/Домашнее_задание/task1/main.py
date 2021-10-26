def func_number():
    list_number = []

    while True:
        number = int(input('Введите число: '))
        if number >= 0:
            if 3 < number < 13:
                list_number.append(number)
        else:
            break

    print('------')

    return list_number


if __name__ == "__main__":

    print(func_number())
