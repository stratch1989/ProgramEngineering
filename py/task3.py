val = int(input())
if val >= 0 and val <= 3:
    print("Первый диапозон")
elif val > 3 and val < 6:
    print("Второй диапозон")
elif val >= 6 and val < 11:
    print("Третий диапозон")
else:
    print("Число не входит ни в один диапозон")