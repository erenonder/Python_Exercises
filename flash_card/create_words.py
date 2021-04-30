

# vocabulary_list = []
# with open("nl_50k.txt", "r") as data_file:
#     for n in range(5000):
#         content = data_file.readline()
#         word = content.split()[0]
#         vocabulary_list.append(word)


# with open("words_5000.txt", "w") as word_file:
#     for word in vocabulary_list:
#         word_file.write(f"{word}\n")

with open("translations.csv", "r") as translation_file:
    content = translation_file.read()


for translation in content.split():

    translation.split(",")
