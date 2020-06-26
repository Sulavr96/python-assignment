def remove_char(string, index):
    return string[:index] + string[index + 1:]


given_string = input("Enter a string: ")
char_index = int(input("Enter the index of character you want to remove: "))

new_string = remove_char(given_string, char_index)

print(new_string)
