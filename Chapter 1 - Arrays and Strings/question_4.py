# Write a method to replace all spaces in a string with'%20'. You may assume that
# the string has sufficient space at the end of the string to hold the additional
# characters, and that you are given the "true" length of the string. (Note: if implementing
# in Java, please use a character array so that you can perform this operation
# in place.)
#
# EXAMPLE
# Input: "Mr John Smith
# Output: "Mr%20Dohn%20Smith"

def encode_string(s):
  return s.rstrip().replace(' ', '%20')

r1 = encode_string("tigers lemmons pie")
r2 = encode_string("dylan harness    ")

print(r1, r2)
