f = open('task1.txt', 'r')
text = str(f.readlines()).replace(',','').replace('.','').replace('\\n','').replace("'",'').lower()
text1 = list(text.split(' '))
example = 0
word = ""
hWord = 0
for i in text1:
    for y in text1:
        if i == y:
            example += 1
        if example > hWord:
            hWord = example
            word = i
    example = 0
print("Всего слов:", len(text1))
print(f'Самое часто встречаемое слово - "{word}", оно встречается {hWord} раз')
f.close