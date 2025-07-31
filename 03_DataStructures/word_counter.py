# Count frequency of words
sentence = "Sage heals Sage revives Jett dashes"
words = sentence.split()
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

print("Word frequency:", counter)