def check_number_in_range(lower, upper, num):
    if num in range(lower, upper):
        print("The number is in the range")
    else:
        print("The number is not in the range")


check_number_in_range(2, 6, 4)
check_number_in_range(3, 5, 2)
