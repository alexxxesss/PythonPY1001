min_number = 1
max_number = 100
multiplicity = 4

list_ = list(range(min_number, max_number))
list_multi = []
for i in range(len(list_)):
    if list_[i] % multiplicity == 0:
        list_multi.append(list_[i])

print(list_multi)

arithmetic_mean = sum(list_multi) / len(list_multi)

print(arithmetic_mean)