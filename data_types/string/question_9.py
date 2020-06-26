string = input("Enter a string: ")
string_length = len(string)

new_string = string[string_length - 1] + string[1:string_length - 1] + string[0]

print(new_string)
