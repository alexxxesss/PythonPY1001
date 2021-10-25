def remove_whitespace(str_):
    words_list = str_with_space.split()
    new_str_with_space = " ".join(words_list)
    return new_str_with_space


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
