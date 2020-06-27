def get_unique_list(user_list):
    print("Sample list:", user_list)

    unique_list = list(set(user_list))

    print("Unique list: ", unique_list)


get_unique_list([1, 2, 3, 3, 3, 3, 4, 5])
