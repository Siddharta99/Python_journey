sentence = input("Type a sentence: ")
words = sentence.split()
word_count = len(words)
char_count = len(sentence)

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(f"words: {word_count}")
print(f"characters: {char_count}")
print(f"Longest word: {longest}")