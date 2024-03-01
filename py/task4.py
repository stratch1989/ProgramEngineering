import re

ftext = open('task4_1.txt', 'r')
fwords = open('task4_2.txt', 'r')

text = str(ftext.readline())
words = fwords.read().split()

for stopword in words:
    text = re.sub(stopword, lambda x: '*' * len(x.group()), text, flags=re.IGNORECASE)
print(text)

ftext.close
fwords.close