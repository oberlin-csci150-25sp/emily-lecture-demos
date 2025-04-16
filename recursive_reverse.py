"""
# Base case: Simplest/Smallest problem?
rev("z") --> "z"
single character, string of length 1

# How do we make the problem smaller?
string slicing

s = hello
    h   ello
    s[0] + s[1:]

hello
ello
llo
lo
o

hello
hell
hel
he
h

# How do we combine it?
concatenate all the subsolutions
+
return letter of s + reverse of the rest of s

"""

def rev(s):
  # base case
  # not base case
  pass