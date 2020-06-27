arr1 = [2, 4, 6, 8, 10, 12, 14]
arr2 = [3, 6, 9, 12, 15]

intersection = list(filter(lambda x: x in arr1, arr2))

print("Intersection items: ", intersection)
