def insert_string_middle(main_string, inserted_string):
    insert_index = len(main_string) // 2

    return main_string[:insert_index] + inserted_string + main_string[insert_index:]


main_string = input("Enter a string: ")
inserted_string = input("Enter a string you want to insert in middle: ")

print(insert_string_middle(main_string, inserted_string))
