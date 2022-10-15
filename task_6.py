list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0
max_number = list_numbers[max_i]

for i, current_number in enumerate(list_numbers):
    max_number = list_numbers[max_i]
    if current_number > max_number:
        max_i = i
        max_number = list_numbers[max_i]

list_numbers[-1], list_numbers[9] = list_numbers[9], list_numbers[-1]

print(list_numbers)
