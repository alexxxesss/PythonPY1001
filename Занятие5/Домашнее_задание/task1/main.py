def multi_table(num):
    multitable = [[0 for x in range(num)] for y in range(num)]
    lenght = len(str(n ** 2)) + 1

    for row in range(1, num + 1):
        for col in range(1, num + 1):
            multitable[row - 1][col - 1] = row * col
            print(f'{str(multitable[row - 1][col - 1]).rjust(lenght)}', end=' ')
        print()


if __name__ == "__main__":
    n = int(input('Введите число, до которого нужо сделать таблицу умножения: '))
    print()
    multi_table(n)

    print()
    print('----------')
    print()

    lenght = len(str(n**2)) + 2
    width = len(str(n)) + 1
    headers = ' ' * width + ' ' + ''.join([str(x).rjust(lenght) for x in range(1, n + 1)])
    dashes = ' ' * width + ':' + '-' * lenght * n
    body = ''

    for row in range(1, n + 1):
        body += str(row).rjust(width) + ':'
        for col in range(1, n + 1):
            body += str(row * col).rjust(lenght)
        body += '\n'

    print('\n'.join([headers, dashes, body]))
