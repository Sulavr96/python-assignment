string = input("Enter a string ")
string_length = len(string)

if string_length < 2:
    print("Empty string")
else:
    new_string = string[0:2] + string[-2:]

    print(new_string)
