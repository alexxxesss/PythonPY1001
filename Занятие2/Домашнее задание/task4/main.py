if __name__ == "__main__":
    # Write your solution here
    pass
numb_list = [2, 15, 4, 8, 45, 3, 16, 10, 167, 33]
index_max_value = 0
max_value = numb_list[index_max_value]

for index, value in enumerate(numb_list):
    if value > max_value:
        max_value = value
        index_max_value = index

numb_list[index_max_value], numb_list[0] = numb_list[0], numb_list[index_max_value]

print(numb_list)