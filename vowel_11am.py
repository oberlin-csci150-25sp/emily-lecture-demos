# functions lecture
# clicker question 12.0

# TODO: Let's make a set of tests!
def testVowel():
  # print statement # Expected value 
  # Add more examples here!
  print("a", isVowel("a")) # True
  print("o", isVowel("o")) # True
  print("z", isVowel("z")) # False
  print("m", isVowel("m")) # False
  print(5, isVowel(5)) # False
  print("aeiou", isVowel("aeiou")) # True ? (pending)
  return

# # Test each option!
# # A
# def isVowel(char):
# 	for letter in "aeiou":
# 		if letter == char:
# 			return True
# 		else:
# 			return False
#   # idea: assign T/F to a variable, return the variable at the end

# print("testing A:")
# testVowel()

# # B
# def isVowel(char):
# 	for letter in "aeiou":
# 		if letter == char:
# 			return True
#   return False

# print("testing B:")
# testVowel()

# C
def isVowel(char):
  # originally
  # return char == "a" or "e" or "i" or "o" or "u"

  # revised
  return char == "a" or char == "e" or char == "i" or char == "o" or char == "u"

print("testing C:")
testVowel()