def return_new_list(lst):
    new_list = [i ** 3 if i < 0 else 0 for i in lst]
    print(new_list)


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    return_new_list(list_)
