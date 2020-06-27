def list_sum(user_list):
    number_sum = 0

    for i in user_list:
        number_sum += i

    return number_sum


my_list = [8, 2, 3, 0, 7]
print("The sum is:", list_sum(my_list))
