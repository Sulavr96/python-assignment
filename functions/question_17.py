word = input("Enter a word: ")
first_char = input("Enter first char: ")

start_character = lambda a: True if a.startswith(first_char) else False

if start_character(word):
    print("The word starts with the given character")
else:
    print("The word does not start with the given character")
