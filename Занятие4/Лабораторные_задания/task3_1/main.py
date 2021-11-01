# TODO
from collections import Counter
def func_1(str_):
    cnt = Counter(str_.lower())
    for char, values in list(cnt.items()):
        if not char.isalpha():
            del cnt[char]
    return cnt

    # dict_chars = {}
    # for i in str_.lower():
    #     if i.isalpha():
    #         if i in dict_chars:
    #             dict_chars[i] += 1
    #         else:
    #             dict_chars[i] = 1
    # return dict_chars

def func_2(dict_ch):
    dict_per = {}
    for char in dict_ch:
        dict_per[char] = round(dict_ch[char] / sum(dict_ch.values()), 4)
    return dict_per


if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    dict_char = func_1(main_str)
    print(dict_char)
    print(func_2(dict_char))
