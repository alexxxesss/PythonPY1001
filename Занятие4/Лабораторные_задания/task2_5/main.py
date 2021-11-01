def func(num):
    reverse_num = 0
    n = num
    while n != 0:
        remains = n % 10
        reverse_num = reverse_num * 10 + remains
        n = n // 10
    if reverse_num == num:
        return 'Число является палиндромом'
    else:
        return 'Число не является палиндромом'





if __name__ == "__main__":
    number = int(input('Введите число для проверки его на палиндром: '))
    print(func(number))
