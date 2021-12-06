"""
Hacker Rank question:
https://www.hackerrank.com/challenges/itertools-permutations/problem

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

question :
You are given a string S .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
"""
import itertools
from itertools import permutations

String, num = input("Enter the String and the number").split(" ")
print(list(itertools.permutations(String, int(num))))


print(String)
