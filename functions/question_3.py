def list_product(user_list):
    product = 1

    for i in user_list:
        product *= i

    return product


my_list = [8, 2, 3, -1, 7]
print('The product is:', list_product(my_list))
