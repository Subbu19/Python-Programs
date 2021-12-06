import collections

a = [1, 2, 1, 3, 4, 4, 4, 5]
result = collections.Counter(a)

print(dict(result))