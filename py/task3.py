f = open('task3.txt', 'r')
strings = 0
letters = 0
words = 0
for i in f.readlines():
    strings+=1
    string = i
    word = string.replace(".", "").rstrip().split(" ")
    for y in word:
        words+=1
        for letter in y:
            letters+=1
print("Input file contains:")
print(letters, "letters")
print(words, "words")
print(strings, "lines")
f.close