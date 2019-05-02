""""CP1404 Prac Task 3
Word Occurrence """

# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
word_count = {}

words = text.split()
for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1

words = list(word_count)

print(words)
for word in words:
    print("{:{}}:{}".format(word, word_count[word]))

