list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def listsToSet(list):
    setFromList = set(list)
    sortSet = set()
    for i in setFromList:
        countDigit = list.count(i)
        sortSet.add(i)
        for y in range(2, countDigit+1):
            sortSet.add(str(i)*y)
    print(sortSet)
    
listsToSet(list_1)
listsToSet(list_2)
listsToSet(list_3)