list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def modifyList(list):
    for _ in range(list.count(2)):
        list.remove(2)
    for index, item in enumerate(list):
        if item == 3:
            list[index] = 4
    return list

print(modifyList(list1))
print(modifyList(list2))
print(modifyList(list3))