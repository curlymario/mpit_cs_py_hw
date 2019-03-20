def max2(x, y):
  if x > y:
    return x
  return y

def max3(x, y, z):
  return max2(x, max(y, z))

print(max3(5, 2, 7))
print(max3(1.5, 0.2, 17.0))
print(max3(1.5, 0.2, 17))
print(max3('ab', 'abc', 'abd'))
print(max2('кит', 'кот'))