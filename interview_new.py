"""
We need to print the frequency of the repetative words in the same order as in the input.
"""
from collections import Counter

def getfrequency(wordlist):

        result = dict(Counter(wordlist))
        print(len(result))
        for i in result.values():
                print(i, end=" ")


if __name__ == '__main__':
        n = int(input())
        wordlist = []
        sum=0
        for i in wordlist:
                wordlist.append(input())
                sum += len(i)
        if n <= 10**5 and sum <= 10**6:
                getfrequency(wordlist)


