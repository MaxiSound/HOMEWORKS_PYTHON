import random


def main():

    tosses = int(input("Сколько раз будем подбрасывать монету?\n"))
    coin(tosses)
    eagle, tails, count = coin(tosses)
    return eagle, tails


def coin(tosses):
    count = 0
    eagle = 0
    tails = 0
    for toss in range(tosses):

        if random.randint(1, 2) == 1:
            print('Орёл')
            eagle += 1
            count += 1
        else:
            print('Решка')
            tails += 1
            count += 1
    return eagle, tails, count

eagle, tails = main()
print('Орёл выпал', eagle, 'раз.')
print('Решка выпала', tails, 'раз')

# Для подсчёта подряд выпавших:
# s = input().split('О')
# res = max(s, key=len)
# print(len(res))
