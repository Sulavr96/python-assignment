word = input("Enter a word: ")

word_length = len(word)

if word_length < 3:
    print(word)
else:
    if 'ing' in word:
        print(word + 'ly')
    else:
        print(word + 'ing')
