# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2):
  return set(s1) == set(s2)

r1 = is_permutation("tigers", "dylan harness")
r2 = is_permutation("tigers", "tigsre")

print(r1, r2)
