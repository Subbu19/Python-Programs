# arr = [1, 2, 3, 5]
#generate 3 digit numbers in which adjacent shld not be same 121 [1,2,1] [1,2,3] but not [1,1,2] or [1,2,2]

from itertools import permutations

arr = [1, 2, 3, 2, 5]

result = permutations(arr, 3)
output = list()
for i in result:
        temp = list(i)
        if temp[0] != temp[1] and temp [1] != temp[2] :
                if temp not in output:
                        output.append(temp)


output2 = list()
output3 = list()

for i,a in enumerate(arr):
        for j,b in enumerate(arr[i+1:]):
                if b !=a and b not in arr[:j]:
                        for k,c in enumerate(arr[j+1:]):
                                if c != b and c not in arr[:k]:
                                        output3.append([a, b, c])

#old result [[1, 2, 3], [1, 2, 5], [1, 3, 2], [1, 3, 5], [1, 2, 5], [2, 3, 2], [2, 3, 2], [2, 3, 5], [2, 5, 2], [3, 2, 3], [3, 2, 5], [3, 5, 3], [3, 5, 2], [2, 5, 2], [2, 5, 3], [2, 5, 2]]
print(len(output3))
print(output3)


#arr = [1, 2, 3, 2, 5]
# 2nd loop = [1,2,3,2,5]
# 2 , j+1 = 2
# 3rd loop = [1,2,4,3,3,2,5]