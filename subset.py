from itertools import combinations
b = [5, 9, 10, 11, 12, 45]
a = list(range(1, 6))

subsets = [list(combinations(b, i)) for i in a]
maxsum = 28
result = []

for i in subsets:
        for j in i:
                print(j, " Sum = ", sum(j))
                if maxsum == sum(j):
                        result.append(j)

print(subsets)
print("result = ", result)
