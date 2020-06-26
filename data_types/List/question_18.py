number_list = [2, 10, 23, 12, 14]
max_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number


print(f'The largest number is: {max_number}')
