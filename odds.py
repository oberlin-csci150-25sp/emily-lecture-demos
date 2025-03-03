# functions lecture
# clicker question 12.3

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

a = largeOdd(97) # None (blank/empty output)
b = findOdds(5) # two lines: 1 is odd [newline] 3 is odd
c = isOdd(2) # False
print(a, b, c)