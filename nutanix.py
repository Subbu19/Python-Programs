#import itertools
from time import perf_counter
a = [1, 3, 1, 5, 6]
b = [1, 5, 9]
c = ["Bala", "Subbuu", "gojjuuuuu"]
c.sort(key=len)
print(c)
#result = {1 : 3, 3 : 1, 5:2, 6:1, 9:1}
result = {}

if len(a) < len(b):
        a, b = b, a

start = perf_counter()

for _ in range(10):
        print("hello world")

for i,value in enumerate(a):
        result[value] = a.count(value) + b.count(value)
        if i < len(b):
                result[b[i]] = a.count(b[i]) + b.count(b[i])
stop = perf_counter()
print(result)
print((stop - start))



