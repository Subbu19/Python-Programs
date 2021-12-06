import threading
import concurrent.futures as cf
import time


def function1(a,b,c):
        print("from Function 1 ")
        time.sleep(3)

def function2():
        print("this is function 2")
        time.sleep(3)
s = time.perf_counter()
#t1 = threading.Thread(target=function1, args=[5, 10, 5])
#t2 = threading.Thread(target=function2)

with cf.ThreadPoolExecutor() as e:
        #submit will create a thread and close it. it will return an object of type thread
        #to access any data returned by the function you have to use .result() function
        response = e.submit(function1, [1, 2, 3])
        response.result()

#

f = time.perf_counter()
print(f'the time taken is {f-s}')
print("End of script")