def numb(num):
    list_num = [int(i) for i in str(num)]
    if 9 < sum(list_num) < 100:
        return "Сумма цифр числа является двухзначным числом!"
    else:
        return "Сумма цифр числа НЕ является двухзначным числом!"


if __name__ == "__main__":
    a = int(input("Введите трехзначное число: "))
    print('-----')
    print(numb(a))
