numbers = input("Enter a list of numbers separated by space ")

number_list = numbers.split()
product = 1

for number in number_list:
    product = product * int(number)

print(product)
