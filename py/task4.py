def main(value, general, i):
    i += 1
    value = int(input("Введите число для расчета среднего ариметического: "))
    general += value
    print("Среднее ариметическое:", general/i)
    main(value, general, i)

if __name__ == '__main__':
    main(0, 0, 0)