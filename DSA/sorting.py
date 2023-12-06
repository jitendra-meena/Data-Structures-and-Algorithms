

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



'''
Selection Sort Algorithm

Selection sort is a sorting algorithm that selects the smallest element
            from an unsorted list in each iteration and places that
                                   element at the beginning of the unsorted list.


'''

'''
Selection Sort Complexity

Time Complexity	 
Best	O(n2)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	No
'''

l1 = [12,3,4,22,44,33,66,44]


for i in range(l):
    min = i
    for j in range(i,l):
        if l1[j] < l1[min]:
            min = j
    l1[i],l1[min]=l1[min],l1[i]
    print(l1)
    
print(l1," _________________selection Sort___________________ ")   





# Insertion Sort 

l3 = [12,323,42,2,44,33,66,44,1]

for i in range(len(l3)):
    key = l3[i]
    j = i-1
    while j>=0 and key < l3[j]:
        l3[j+1] = l3[j]
        j -= 1
    l3[j+1] = key
print(l3," _________________Insertion Sort___________________ ")  



def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList," _________________Merge Sort___________________ ")   


