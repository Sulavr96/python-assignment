marks = [{'name': 'ram', 'roll': 12, 'mark': 60}, {'name': 'shyam', 'roll': 10, 'mark': 70},
         {'name': 'gita', 'roll': 5, 'mark': 45}]

print('Unsorted_marks:', marks)

sorted_marks = sorted(marks, key=lambda x: x['mark'])

print('Sorted marks:', sorted_marks)
