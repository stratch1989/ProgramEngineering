myList = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865,
           5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439,
           9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193,
           9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

print('Кол-во чеков:',len(myList))
print('Кол-во разных людей:',len(set(myList)))

superWorker = 0
searcherMax = 0
max = 0

for i in myList:
    for y in myList:
        if i == y:
            searcherMax += 1
    if max < searcherMax:
        superWorker = i
        max = searcherMax
    searcherMax = 0

print(f"Больше всего раз посетил: {superWorker}, кол-во раз: {max}")