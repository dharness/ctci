# Implement a function void reverse(char* str) in C or C++ which reverses a nullterminated
# string.

def reverse_string(s):
  return ''.join(reversed(s))

r1 = reverse_string("tigers")
r2 = reverse_string("dylan harness")

print(r1, r2)
