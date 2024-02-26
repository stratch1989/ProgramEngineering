import random

def main(digit):
    if digit == 5 or digit == 6:
        print("Вы победили")
    elif digit == 1 or digit == 2:
        print("Вы проиграли")
    else: main(random.randint(1,6))

if __name__ == '__main__':
    main(random.randint(1,6))