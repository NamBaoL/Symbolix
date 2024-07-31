# [a, b, c, ...] ==> [a b c ...]
def listFormat(array):
  return str(array).replace(',', '')

# [f, g, h, ...] ==> (f g h ...)
def funcFormat(block):
  return f'({str(block)[1:-1].replace(',', '')})'

print(funcFormat([3, 4, 5, 6, "Hello", [3, 4]]))