def greatest_among_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


greatest_number = greatest_among_three(5, 4, 10)
print('The greatest number is:', greatest_number)
