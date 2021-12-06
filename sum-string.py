"""
Given a string of digits, the task is to check if it is a ‘sum-string’.
A string S is called a sum-string if a rightmost substring can be written as a sum of two substrings before it and the
same is recursively true for substrings before it.

Eg : 1
Input:
        12243660
Output:
        1
Explanation:

"12243660" is a sum string. As we
can get, 24 + 36 = 60 & 12 + 24 = 36.

"""
from itertools import combinations as c , permutations as p

string = input()

combo = p(string, )
print(list(combo))

a = range(1, 6)
b = ['a', 'b', 'c', 'd', 'e']
c = dict(zip(a, b))
print(c)