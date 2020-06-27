integer_list = [5, 2, 20, 1, 8, 3, 12]

even_integers = list(filter(lambda a: a % 2 == 0, integer_list))

print("Even integers: ", even_integers)

odd_integers = list(filter(lambda a: a % 2 != 0, integer_list))

print("Odd integers: ", odd_integers)
