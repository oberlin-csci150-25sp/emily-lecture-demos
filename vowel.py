# functions lecture
# clicker question 12.2

# TODO: Let's make a set of tests!
# print statement # Expected value 
# print(isVowel("red")) # ??
# print(isVowel("w")) # ??
# print(isVowel("o")) # ??
# print(isVowel(2)) # ??

# TODO: Test each option!
# A
def isVowel(char):
	for letter in "aeiou":
		if letter == char:
			return True
		else:
			return False

print("testing A:")
# ADD TEST PRINTS HERE

# B
def isVowel(char):
	for letter in "aeiou":
		if letter == char:
			return True
	return False

print("testing B:")
# ADD TEST PRINTS HERE


# C
def isVowel(char):
	return char == "a" or "e" or "i" or "o" or "u"

print("testing C:")
# ADD TEST PRINTS HERE