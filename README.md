# Data-Structures-and-Algorithms
data structures and algorithms using Python



# Data Stuctures:


A data structure is a specialized format for organizing, processing, retrieving and storing data. There are several basic and advanced types of data structures, all designed to arrange data to suit a specific purpose. Data structures make it easy for users to access and work with the data they need in appropriate ways


# Data-Structures using Python :

![Register](https://github.com/jitendra-meena/Data-Structures-and-Algorithms/blob/main/DSA.jpeg)

# Bubble Sort Complexity
 ```bash

Time Complexity	 
Best	O(n)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	Yes
Complexity in Detail
Bubble Sort compares the adjacent elements.

Cycle	Number of Comparisons
1st	(n-1)
2nd	(n-2)
3rd	(n-3)
.......	......
last	1
Hence, the number of comparisons is

(n-1) + (n-2) + (n-3) +.....+ 1 = n(n-1)/2
nearly equals to n2

Hence, Complexity: O(n2)

Also, if we observe the code, bubble sort requires two loops. Hence, the complexity is n*n = n2
```
# Time Complexities
 ```bash

Worst Case Complexity: O(n2)
If we want to sort in ascending order and the array is in descending order then the worst case occurs.
Best Case Complexity: O(n)
If the array is already sorted, then there is no need for sorting.
Average Case Complexity: O(n2)
It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
```
# Space Complexity
 ```bash

Space complexity is O(1) because an extra variable is used for swapping.
In the optimized bubble sort algorithm, two extra variables are used. Hence, the space complexity will be O(2)
```
# Selection Sort Complexity
 ```bash
Time Complexity	 
Best	O(n2)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	No
Cycle	Number of Comparison
1st	(n-1)
2nd	(n-2)
3rd	(n-3)
last	1
Number of comparisons: (n - 1) + (n - 2) + (n - 3) + ..... + 1 = n(n - 1) / 2 nearly equals to n2.
```
# Complexity = O(n2)

Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity is n*n = n2.

# Time Complexities:
 ```bash

Worst Case Complexity: O(n2)
If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
Best Case Complexity: O(n2)
It occurs when the array is already sorted
Average Case Complexity: O(n2)
It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
```