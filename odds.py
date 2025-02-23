# functions lecture
# clicker question 12.1

def isOdd(num):
    remainder = num % 2
    return remainder == 1

def findOdds(num):
    for n in range(num): # 0 1 2 3 4
        if isOdd(n):
            print(n, "is odd")

def largeOdd(num):
    if num < 100:
        return
    else:
        return isOdd(num)

a = largeOdd(97)
b = findOdds(5)
c = isOdd(2)
print(a, b, c)