string = input("Enter a sentence: ")

if 'not' in string and 'poor' in string:
    not_word_index = string.find('not')
    poor_word_index = string.find('poor')

    new_string = string[:not_word_index] + 'good' + string[poor_word_index + 4:]
    print(new_string)

else:
    print(string)
