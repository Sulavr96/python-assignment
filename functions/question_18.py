string = input("Enter a string: ")

check_string = lambda x: True if string.isnumeric() else False

if check_string(string):
    print("Given string is number")
else:
    print("Given string is not number")
