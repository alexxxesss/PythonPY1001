def main():
    sqrt_list = []
    count = 0

    while sum(sqrt_list) < 500:
        sqrt_list.append(count**2)
        print(f'Список: {sqrt_list}')
        print(f'Сумма его квадратов: {sum(sqrt_list)}')
        count += 1
    print("------")
    return print('Количество чисел: ' + str((len(sqrt_list)) - 1))

# def main():
#     sqrt_list = []
#     count = 0
#
#     while True:
#         if sum(sqrt_list) > 500:
#             return len(sqrt_list[:-1])
#         else:
#             sqrt_list.append(count ** 2)
#             print(f'Список: {sqrt_list}')
#             print(f'Сумма его квадратов: {sum(sqrt_list)}')
#             count += 1


if __name__ == "__main__":
    main()