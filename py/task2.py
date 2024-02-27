tpl1 = (1, 2, 3), 1
tpl2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3
tpl3 = (2, 4, 6, 6, 4, 2), 9

def remove_element(tpl, remInd):
    modList = list(tpl)
    if remInd in tpl:
        modList.remove(remInd)
    return tuple(modList)

print("Первый кортеж:", remove_element(tpl1[0], tpl1[1]))
print("Второй кортеж:", remove_element(tpl2[0], tpl2[1]))
print("Третий кортеж:", remove_element(tpl3[0], tpl3[1]))