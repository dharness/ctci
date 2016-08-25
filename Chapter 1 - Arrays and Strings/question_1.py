# Implement an algorithm to determine if a string has all unique characters. What
# if you cannot use additional data structures?

def string_contains_unique(s):
  return len(set(s)) == len(s)

r1 = string_contains_unique("lemmons")
r2 = string_contains_unique("lemons")

print(r1, r2)
