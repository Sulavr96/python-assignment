def get_even_list(user_list):
    print('Given list: ', user_list)
    even_list = []
    for number in user_list:
        if number % 2 == 0:
            even_list.append(number)

    print('Even list: ', even_list)


get_even_list([1, 2, 3, 4, 5, 6, 7, 8])
