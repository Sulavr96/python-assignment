string = input("Enter two strings separated by space: ")

first_string, second_string = string.split(" ")

new_first_string = second_string[:2] + first_string[2:]
new_second_string = first_string[:2] + second_string[2:]

print(f'{new_first_string} {new_second_string}')
