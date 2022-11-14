import random
from random import randint
def get_unique_list_numbers(x=-10, y=10, l=15) -> list[int]:
    list = []
    while len(list) < l:
        digit_ = random.randint(x, y)
        if digit_ not in list:
            list.append(digit_)
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))