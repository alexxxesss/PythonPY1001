if __name__ == "__main__":
    def polindrom(str_):
        str_low = str_.lower()
        new_str = str_low[::-1]
        if new_str == str_low:
            return "Эта строка является палиндромом"
        else:
            return "Эта строка не палиндром"



    check_word = input("Введите слово для проверки: ")

    print("------")
    print(polindrom(check_word))