# goal: convert f to c temperatures
# example: 0c --> 32f

# input
c = input("What's the temperature in C? ")

# work
f = int(c)*9//5+32

# output
print("The temperature today is", str(f))