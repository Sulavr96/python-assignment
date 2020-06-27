integer_list = [1, 2, 3, 5, 6, 7]

print("Original list: ", integer_list)

squared_integer_list = map(lambda x: x**2, integer_list)

print('Squared list:', list(squared_integer_list))

cubed_integer_list = map(lambda x: x**3, integer_list)

print('Cubed list:', list(cubed_integer_list))
