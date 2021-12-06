# Example 1: Input : [1,2,3], target = 4

# Output : [[1,1,1,1],[1,3],[2,2],[1,1,2]

from itertools import combinations as c

def arraysum(input, target):

        result = list()
        for i in input:
                if (target - i) in input:
                        result.append([i, target-i])
                temp = []
                for j in input:
                        if j + i == target
                recursivearray(i, target)
                print(temp)




def recursion(number, temp=list()):

        if number == 100:
                return temp
        else:
                #print(number)
                temp.append(number)
                return recursion(number + 1)


if __name__ == '__main__':
        a = [1, 2, 3]
        target = 4
        #arraysum(a, target)
        print(recursion(2))
