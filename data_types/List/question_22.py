user_input = input("Enter items separated by comma to be inserted in a list: ")
user_list = user_input.split(", ")

user_list_without_duplicate = list(dict.fromkeys(user_list))

print(user_list_without_duplicate)
