sentence = input("Enter a sentence: ")
word_list = sentence.split()
word_collection = {}

for word in word_list:
    if word in word_collection:
        word_collection[word] += 1
    else:
        word_collection[word] = 1

print(word_collection)
