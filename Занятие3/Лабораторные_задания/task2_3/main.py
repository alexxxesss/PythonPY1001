if __name__ == "__main__":

    def func(str_slov):
        list_slov = str_slov.split()
        set_slov = set(list_slov)

        for word in set_slov:
            print(word)

    str_word = input('Введите несколько слов через пробел: ')

    print("-----")
    func(str_word)
