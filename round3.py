# From a given sorted integer array and an integer i, find a pair in array whose sum is closest to i
#
# Input: arr[] = {10, 22, 28, 29, 30, 40}, i = 54
# Output: [22,30]

def closestsum(arr, s):

        dictsum = dict()
        for k, i in enumerate(arr):
                #print(k, i)
                if i > s:
                        break
                for j in arr[k+1:]:
                        temp = s-j-i

                        if temp < 0:
                                temp *= -1
                        dictsum[temp] = [i, j]

        pair = min(dictsum.keys())
        print(dictsum[pair])

if __name__ == '__main__':
        arr = [10, 22, 28, 29, 30, 32, 33, 40, 65]
        summ = 54

        closestsum(arr, summ)