if __name__ == "__main__":

    count_whitespace = 4
    whitespace = " "
    str_ = 'Hello, world'

    for i in range(len(str_)):
        count_whitespace += 1
        print(whitespace * count_whitespace + str_[i])


    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой

    count_whitespace = 5
    whitespace = " "
    str_ = 'Hello, world'

    for i in range(len(str_)):
        if i < 1:
            print(whitespace * count_whitespace + str_[i])
        else:
            count_whitespace += 1
            print(whitespace * count_whitespace + str_[i])