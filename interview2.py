"""
we have a sentence, in this find the words and its frequency.

S = "my name is subhash"

"""

def getfrequency(sentence):

        wordlist = sentence.split(" ")
        frequency = {}
        for i in wordlist:
                frequency[i] = wordlist.count(i)
        print(frequency)

        non_repeating = []
        for i in sentence:
                if sentence.count(i) == 1:
                        non_repeating.append(i)
        print(non_repeating)


def palindrome(sentence):

        if sentence == sentence[::-1]:
                print("the whole sentence is palindrome ")
        else:
                wordlist = sentence.split(" ")
                palindromelist = []
                for i in wordlist:
                        if i == i[::-1] and i.isalnum():
                                palindromelist.append(i)
                if len(palindromelist) > 0:
                        print(palindromelist)
                else:
                        print("there are no Palindromes in the list")


sentence = "this is my name \n my native is Kolar isi "
getfrequency(sentence)
palindrome(sentence)