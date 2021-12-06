#N number of students :

students_names = ["Subhash", "Suhas", "Sudarshan", "Su", "Su", "Suhas", "Su", " ",""]
def oldcode():
        max_length = 0
        #max_length = len(max(students_names))
        students_names.sort()
        prefix_length = {}

        for ele in students_names:
                for i in range(len(ele)+1):
                        substring = ele[0:i]
                        counter = 0
                        for j in students_names:
                                if j[0:i] == substring:
                                                counter += 1
                        if counter > 1:
                                prefix_length[substring] = len(substring)

def largestprefix(names):

        names.sort(key=len)
        prefix = ""
        for i in range(len(names[0])):
                prefix = names[0][0:i]
                for j in names:
                        if j[0:i] == prefix:
                                continue
                        elif i> 0:
                                return prefix[0:i-1]
        return prefix

print(largestprefix(students_names))
#print(max(prefix_length.keys()))
s= "abc"

