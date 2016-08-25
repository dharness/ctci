# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string.

def compress_string(s):
  compressed = []
  count = 0
  for i, ch in enumerate(s):
    if (i > 0 and s[i-1] == ch):
      count = count + 1
    else:
      if (count > 0):
        count = 0
        compressed.append(str(count))
      compressed.append(ch)
      count = count + 1
  compressed.append(str(count))
  return ''.join(compressed)

# r1 = compress_string("tigers lemmons pie")
r2 = compress_string("aabcccccaaa")

print(r2)
