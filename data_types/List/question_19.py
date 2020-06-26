number_list = [20, 15, 23, 12, 14]

min_number = number_list[0]

for number in number_list:
    if number < min_number:
        min_number = number

print(f'The smallest number is: {min_number}')
