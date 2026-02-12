# reading a text file and preforming basic text processing before computing word statistics

# import library re
import re

# read the file "sample-file.txt"
with open ("sample-file.txt", "r") as file:
    content = file.read()

# take only words and exclude punctuation
tokens_without_punctuation_and_only_lower_case = re.findall(r"\w+", content)

# make all the tokens lower case
tokens_without_punctuation_and_only_lower_case = [token.lower() for token in tokens_without_punctuation_and_only_lower_case]

# remove any tokens with a length <= 2
tokens_with_length_greater_than_2 = [token for token in tokens_without_punctuation_and_only_lower_case if len(token) > 2 ]

# count the word frequencies and print the most frequent words in descending order in the format: word ---> count
word_counter = {}

for word in tokens_with_length_greater_than_2:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

# sort most frequent words in descending order
most_frequent_words_in_descending_order = sorted(word_counter.items(), key = lambda x: x[1], reverse = True)

# print the 10 most frequent words
for word, count in most_frequent_words_in_descending_order[:10]:
    print(f"{word} ---> {count}")