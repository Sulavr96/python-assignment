string = input("Enter a given string: ")
new_string = ''

for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]


print(new_string)
