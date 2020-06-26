list_1 = [{}, {}, {}]
list_2 = [{2, 3}, {4, 5}, {}]

is_list1_empty = True
is_list2_empty = True

for item in list_1:
    if len(item) != 0:
        is_list1_empty = False

print("Is list 1 is empty?:", is_list1_empty)

for item in list_2:
    if len(item) != 0:
        is_list2_empty = False


print("Is list 2 is empty?:", is_list2_empty)
