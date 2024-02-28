nums = input('Введите числа\n')

def add(nums): 
    dictionary = dict()
    for i in nums:
        dictionary[i] = len(nums)
    sortedDict = sorted(dictionary.items(), key=lambda item: item[0])
    print("Цифры в порядке возрастания:", dict(sortedDict).keys())
    return dictionary

def func(nums):
    dictionary = add(nums)
    print(dictionary)
func(nums)