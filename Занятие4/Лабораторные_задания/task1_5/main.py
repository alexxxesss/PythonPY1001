if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    even_number = [i for i in list_ if i % 2 == 0]
    odd_number = [i for i in list_ if i % 2 != 0]

    if len(even_number) > len(odd_number):
        print("Четных чисел в списке больше")
    elif len(even_number) == len(odd_number):
        print("Четных и нечетных чисел в списке одинаково")
    else:
        print('Нечетных чисел в списке больше')
