"""
we will have 1 string.
Create 2 strings
1st list whose name is Stuart will have all the substrings starting with a consonant.
2nd list whose name is kevin will have all the substrings starting with a vowel.
"""
from collections import Counter
word = "BANANA"
stuart = []
kevin = []
vowels = ["A","E","I","O","U"]

for i in range(1, len(word)+1):
        for j in range(len(word), i-1, -1):
                substring = word[i-1:j]
                if substring[0] in vowels:
                        kevin.append(substring)
                else:
                        stuart.append(substring)

ksum = sum(list(Counter(kevin).values()))
ssum = sum(list(Counter(stuart).values()))

if ksum > ssum :
        print("kevin", ksum)
else:
        print("Stuart", ssum)

