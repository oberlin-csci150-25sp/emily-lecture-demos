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
  print(s)
  if len(s) == 1:
    return s
  # return s[-1] + rev(s[:-1])
  return rev(s[1:]) + s[0]

def main():
  print(rev("hello"))
  print(rev("racecar"))
  print(rev("e"))

main()