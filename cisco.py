#create a list of 1 to 10 in any order, use random,

import random


def mysorting(a):
        for i in range(len(a)):
                key = a[i]
                #print(" =", key )
                pos = i
                for j in range(i, len(a)):
                        if a[j] < key:
                                key = a[j]
                                pos = j
                #print("Exchanging this ", a[i], a[pos])
                a[i], a[pos] = a[pos], a[i]
                #print("After exchange a[i]  a[pos]", a[i], a[pos])

        print("Sorted list", a)


def mybinarysearch(a, key):
        #mid = (len(a)/2)-1
        top = len(a)-1
        bottom = 0
        mid = (top-bottom)//2
        n = top+bottom % 2
        print("mid = ", mid)
        while mid > 0 :
                if a[mid] == key:
                        return True, mid
                elif a[mid] < key :
                        bottom = mid +1
                else:
                        top = mid -1
                #print("Top = ", top)
                #print("bottom = ", bottom)
                mid = (top+bottom)//2
                print(mid)
        return False, None






if __name__ == '__main__':

        a =[]
        #a = [random.randint(0,10) for i in range(10) if True print(i) ]
        counter=0
        while counter<10:
                temp = int(random.random() * 10)
                if temp in a:
                        continue
                else:
                        a.append(temp)
                        counter +=1
        #sort the list Quick sort
        print("this is the list that is generated: ", a)
        mysorting(a)
        key = int(input("Enter the number to be searched"))
        pos, result = mybinarysearch(a, key)
        if result:
                print("Number found in the list", pos)
        else:
                print("Number not found")
        #print(a)
