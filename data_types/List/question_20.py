strings = input("Enter strings having length 2 or more separated by comma: ")
string_list = strings.split(", ")
word_count = 0

for string in string_list:
    string_length = len(string)

    if string[0] == string[string_length - 1]:
        word_count += 1

print(f'Number of words with repeated first and last character is: {word_count}')
