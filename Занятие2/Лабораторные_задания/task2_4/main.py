if __name__ == "__main__":

    count_whitespace = 5
    whitespace = " "
    str_ = 'Hello, world'

    for i in range(len(str_)):
        print(whitespace * count_whitespace + str_[i])
        count_whitespace += 1


    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой
