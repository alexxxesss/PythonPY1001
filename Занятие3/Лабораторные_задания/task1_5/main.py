if __name__ == "__main__":

    def func_sum():

        count = None
        list_count = []

        while count != 0:
            count = int(input('Введите число: '))
            if count > 0:
                list_count.append(count)

        print('-----')
        return sum(list_count)

    print(f'Ссума положительных введенных чисел равна {func_sum()}')
