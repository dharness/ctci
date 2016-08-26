# Write an algorithm such that if an element in an MxN matrix is 0, its entire row
# and column are set to 0.

def minesweeper(m):
  mines = {'xs': [], 'ys': []}
  for y, row in enumerate(m):
    for x, el in enumerate(row):
      if(el == 0):
        mines['xs'].append(x)
        mines['ys'].append(y)

  for y, row in enumerate(m):
    for x, el in enumerate(row):
      if (y in mines['ys']):
        m[y][x] = 0
      elif (x in mines['xs']):
        m[y][x] = 0
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

r1 = minesweeper(matrix)

for row in r1:
  print(row)
