number_of_elements = int(input("How many elements?: "))

new_dictionary = {x: x**2 for x in range(1, number_of_elements + 1)}

print(new_dictionary)
