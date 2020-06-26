user_input = input("Enter items separated by comma to be inserted in a list: ")
user_list = user_input.split(", ")

added_string = input("Enter a string to be added to the items in the list: ")
new_list = []

for item in user_list:
    new_list.append(item + added_string)

print(new_list)
