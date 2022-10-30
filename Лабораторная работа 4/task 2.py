def get_count_char(str_):
    DEF_COUNT = 0# TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {}
    for letter in str_.lower():
        if letter.isalpha():
            dict_[letter] = dict_.get(letter, DEF_COUNT) + 1
    return dict_

def percent_dict(dict_new):
    sum_ = sum(dict_new.values())
    for letter in dict_new:
        dict_new[letter] = round((dict_new[letter] / sum_) * 100, 2)
    return dict_new

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
result_dict = get_count_char(main_str)
print(percent_dict(result_dict))
