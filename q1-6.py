n = 3;

matrix = [[x]*n for x in range(0, n)]


def rotate(m):
  n = len(m)
  newMatrix = [[p]*n for p in range(0, n)]
  for x, row in enumerate(m):
    for y, el in enumerate(row):
      x2 = n - y - 1;
      y2 = x;
      newMatrix[x2][y2] = el;
  return newMatrix;

# --------------------- TEST ---------------------

for row in matrix:
  print(row)

res = rotate(matrix);
print('-----------------')

for row in res:
  print(row)
