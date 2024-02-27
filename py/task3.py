from math import sqrt 
list1 = [12, 25, 3, 48, 71]
list2 = [5, 18, 40, 62, 98]
list3 = [4, 21, 37, 56, 84]

def calculatingArea(a, b, c):
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

print("Самый большой треугольник:", calculatingArea(max(list1), max(list2), max(list3)))
print("Самый маленький треугольник:", calculatingArea(min(list1), min(list2), min(list3)))