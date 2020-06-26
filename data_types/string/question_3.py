string = input("Enter a string: ")
string_length = len(string)
string_list = list(string)

for i in range(0, string_length):
    if string_list[0] == string_list[i] and i != 0:
        string_list[i] = '$'

new_string = "".join(string_list)
print(new_string)
