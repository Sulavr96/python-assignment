numbers = input("Enter a list of numbers separated by space ")

number_list = numbers.split()
number_sum = 0

for number in number_list:
    number_sum = number_sum + int(number)

print(number_sum)
