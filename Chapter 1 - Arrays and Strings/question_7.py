# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

def zero_out_row(m):
  for i, row in enumerate(m):
    if (0 in row):
      m[i] = [0] * len(row)
  return m

matrix = [
  [1,2,3,4,5],
  [0,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,4,5],
  [1,2,3,0,5],
  [1,2,3,4,5],
  [1,2,3,4,5]
]

r1 = zero_out_row(matrix)

for row in r1:
  print(row)
