# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, si and s2, write code to check if s2 is
# a rotation of si using only one call to isSubstring (e.g.,"waterbottle"is a rotation
# of "erbottlewat").


def is_rotation(original, test):
  end = ''
  if (len(original) != len(test)):
    return False
  for ch in original:
    end += ch
    start = len(test) - len(end)
    word_end = test[start:]
    word_start = test[0:start]
    if (word_end == end  and word_start == original[len(end):]):
      return True
  return False

r1 = is_rotation("waterbottle", "erbottlewat")
r2 = is_rotation("erbottlewat", "waterbottle")
r3 = is_rotation("0011001", "0100110")

# poplol loppop

print(r1, r2, r3)
