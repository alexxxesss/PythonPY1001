def some_func(num):
    list_num = [int(i) for i in str(num)]
    if sum(list_num) % 7 == 0:
        return 'Сумма цифр введенного числа кратна 7'
    else:
        return "Сумма цифр введенного числа не кратна 7"


if __name__ == "__main__":
    a = int(input('Введите четырехзначное число: '))
    print('-----')
    print(some_func(a))
