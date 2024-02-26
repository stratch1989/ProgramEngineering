from math import sqrt 

def calculatingArea(a, b, c):
    p = (a+b+c)/2
    print("Результат:", sqrt(p*(p-a)*(p-b)*(p-c)))