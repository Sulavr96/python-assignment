dict_1 = {'key1': 10, 'key2': 12, 'key3': 14, 'key4': 16}

print("Before deleting: ")
print(dict_1)


def del_dictionary_key(key):
    del dict_1[key]


del_dictionary_key('key2')

print("After deleting: ")
print(dict_1)
