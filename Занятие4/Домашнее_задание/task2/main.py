def func_num(num):
    list_num = [int(i) for i in str(num)]
    print(list_num)
    for i in range(1, len(list_num)):
        if list_num[0] == list_num[i]:
            return "Есть одинаковые цифры в введенном числе"

    return 'Условие задания не выполняется'




if __name__ == "__main__":
    a = int(input('Введите число для проверки: '))
    print('-----')
    print(func_num(a))
