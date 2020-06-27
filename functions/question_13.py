tuple_list = [(15, 23), (12, 14), (16, 13), (11,12)]

sorted_tuple_list_by_first_value = sorted(tuple_list, key=lambda x: x[0])

print("Sorted list by first value of tuple: ")
print(sorted_tuple_list_by_first_value)

sorted_tuple_list_by_second_value = sorted(tuple_list, key=lambda x: x[1])

print("Sorted list by second value of tuple: ")
print(sorted_tuple_list_by_second_value)
