def get_longest_word(words):
    max_length = 0
    longest_word = ''
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            longest_word = word

    return longest_word


word_list = ['apple', 'banana', 'Pomegranate', 'strawberry', 'grapes']

longest_word = get_longest_word(word_list)

print(f'The longest word is {longest_word} and its length is {len(longest_word)}')
