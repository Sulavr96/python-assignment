word = input("Enter a word ")

word_length = len(word)
char_collection = {}

for i in range(word_length):
    char_count = word.count(word[i])
    char_collection.update({word[i]: char_count})

print(char_collection)
