def func_str_word(a):
    list_a = a.split()
    list_size = []

    for i in list_a:
        list_size.append(len(i))

    max_size = max(list_size)

    list_max_word = []

    for i in list_a:
        if len(i) == max_size:
            list_max_word.append(i)

    if len(list_max_word) == 1:
        max_word = list_max_word[0]
        return max_word[::-1]
    else:
        return list_max_word


if __name__ == "__main__":
    str_word = input('Введите строку слов с пробелами (пробелов можеть быть больше чем 1): ')
    print(func_str_word(str_word))
