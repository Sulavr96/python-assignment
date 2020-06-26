my_tuple = 2, 4, 5, 6, 7, 9


def del_from_tuple(value):
    my_tuple_list = list(my_tuple)
    my_tuple_list.remove(value)

    return tuple(my_tuple_list)


print(del_from_tuple(7))
