def func_number(num):
    list_number = [int(x) for x in str(num)]

    print(list_number)
    print(sum(list_number))
    print(sum([i for i in list_number if i % 2 == 0]))
    print(len(list_number))
    print(min(list_number))
    print(max(list_number))
    print([i for i in list_number if list_number.index(i) % 2 != 0])
    print([i for i in list_number if list_number.index(i) % 2 == 0])
    print(list_number[0] - list_number[-1])
    print(f'Минимальное значение {min(list_number)}, стоит на месте {list_number.index(min(list_number)) + 1}')


if __name__ == "__main__":
    N = int(input('Введите число N: '))
    func_number(N)
