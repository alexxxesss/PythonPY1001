list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее уникальных чисел
unique_list = set(list_)
print(sum(unique_list))
print(len(unique_list))
print(sum(unique_list) / len(unique_list))
