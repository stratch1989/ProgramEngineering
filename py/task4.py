test = "The tTEST_ssiis acqwe ooo UuUu, ugly sdfwd qweqwincefvueugly end"

print("Длина текста:", len(test))
lowerText = test.lower()
print("Текст в нижнем регистре:", lowerText)
exampleLetters = "aeiou"
howManyLetters = 0
for u in exampleLetters:
    for i in lowerText:
        if i == u:
            howManyLetters += 1
    print(f"Букв {u} в тексте: {howManyLetters}")
    howManyLetters = 0
print(lowerText.replace('ugly', 'beauty'))
print(test.startswith('The') and test.endswith('end'))