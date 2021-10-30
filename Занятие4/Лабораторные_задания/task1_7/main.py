if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    average_list = sum(list_) / len(list_)
    difference_list = [round(i - average_list, 1) for i in list_]
    print(average_list)
    print(difference_list)
