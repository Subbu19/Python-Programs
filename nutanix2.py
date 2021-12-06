"""
I/P:
3, 7, 8, 9, 10, 14, 15, 20, 21, 22, 30, 31, 40

O/P:
3, 7-10, 14, 15, 20-22, 30, 31, 40


"""

"""
def lstrange(lst):
        op = ""
        start = end = lst[0]  # start and end are range's bounds
        for i in lst[1:]:
                if (i - end) == 1:
                        end = i  # range grows
                else:  # range ended
                        if start == end:
                                op = op + str(start) + ", "
                        else:
                                op = op + str(start) + "-" + str(end) + ","
                        start = end = i
        if start == end:
                op = op + str(start)
        else:
                op = op + str(start) + "-" + str(end)

        return op
"""
def numberRange(ip):
        op = ""
        start = end = ip[0] #start and end are range elements
        #temmp = ""
        for i in ip[1:]:
                if (i - end) == 1:
                        end = i
                        #temmp = temmp + "," + str(i) #using temp to store all the intermediate numbers in case the range required is more than 2
                        #print(temp)
                else:  # range ended
                        if start == end:
                                op = op + str(start) + ", "
                        elif (end - start) == 1: #if the range is 2 we are adding both the numbers as it is
                                #print("range is 2")
                                op = op + str(start) + "," + str(end) + ","
                        else:
                                op = op + str(start) + "-" + str(end) + ","
                        start = end = i
        #this code is to handle the last element (could be last element or last range element )
        if start == end:
                op = op + str(start)
        else:
                op = op + str(start) + "-" + str(end)

        return op

ip = [3, 7, 8, 9, 11, 14, 15, 20, 21, 22, 30, 31, 32]
print(numberRange(ip))
