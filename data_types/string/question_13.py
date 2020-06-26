words = input("Enter words separated by comma: ")
word_list = words.split(", ")

sorted_word_list = sorted(word_list)

print(", ".join(sorted_word_list))
