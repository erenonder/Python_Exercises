from collections import Counter
import re

def count_words(input_file):

    with open(input_file, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]

    word_counter = Counter()

    for word in all_words:
        word_counter[word] += 1

    common_words = word_counter.most_common(20)

    total_words = sum(word_counter.values())

    print(f'\nTotal Words: {total_words}')

    print('\nTop 20 Words')
    for word_tuple in common_words:
        print(f'{word_tuple[0]:10} {word_tuple[1]}')


count_words('test_file.txt')
