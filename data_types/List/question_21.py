list_with_tuples = [(2, 3), (1, 2), (3, 5), (4, 1), (5, 4), (6, 6)]

sorted_list_with_tuple = sorted(list_with_tuples, key=lambda n: n[1])
print(sorted_list_with_tuple)
