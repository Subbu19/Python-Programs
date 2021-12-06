a = "ABCD"
import itertools

for i in range(len(a)):
        c= tuple(itertools.permutations(a,i) )
        print(c)


a = set()
a.add("abc")
a.update("def")
print(a)
