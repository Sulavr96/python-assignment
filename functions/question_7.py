def calculate_upper_and_lower_char(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char != " ":
            if char.isupper():
                upper_count += 1
            else:
                lower_count +=1

    print("The number of upper case character:", upper_count)
    print("The number of lower case character:", lower_count)


calculate_upper_and_lower_char("The quick Brown Fox Jumped Over")
