def func_num(num):
    list_num = [int(i) for i in str(num)]

    if sum(list_num[:3]) == sum(list_num[3:]):
        return "Это число самое счастливое)"

    return 'Увы, тебе не повезло('


if __name__ == "__main__":
    a = int(input('Введите шестизначное число и узнаете, являетлся ли оно счастливым))): '))
    print('-----')
    print(func_num(a))

