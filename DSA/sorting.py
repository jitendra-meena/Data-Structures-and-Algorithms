

'''
Bubble Sort Python Program

A Python bubble sort goes through a list and compares elements next to each other.
     If an element on the right is greater than one on the left, the elements are swapped.
        This happens until the list is sorted.


'''



'''
Ascending Order 
'''
l1 = [12,33,44,22,44,33,66,44]

l = len(l1)
for i in range(0,l):
    for j in range(0,l-i-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)




'''
Descending Order 
'''
l1 = [12,33,44,22,44,33,66,44]

l = len(l1)
for i in range(0,l):
    for j in range(0,l-i-1):
        if l1[j]<l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)