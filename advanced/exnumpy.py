# $ pip install numpy

import numpy as np

list1 = [1,2,3,4]
a = np.array(list1)
print(a)
print(a.shape)

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
print(b[0,0])

a = np.zeros((2,2))
print(a)

a = np.ones((2,3))
print(a)

a = np.full((2,3),5)
print(a)

a = np.eye(3)
print(a)

a = np.array(range(20)).reshape((4,5))
print(a)

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
a = arr[0:2, 0:2]
print(a)

a = arr[1:, 1:]
print(a)

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
s = a[[0, 2], [1, 3]] 
print(s)

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
bool_indexing_array = np.array([
    [False,  True, False],
    [True, False,  True],
    [False,  True, False]
]) 
n = a[bool_indexing_array];
print(n)    

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
bool_indexing = (a % 2 == 0)
 
print(bool_indexing) 

print(a[bool_indexing])

n = a[ a % 2 == 0 ]
print(n)

a = np.array([1,2,3])
b = np.array([4,5,6])
 
c = a + b
print(c)  
 
c = a - b
# c = np.subtract(a, b)
print(c) 
 
# c = a * b
c = np.multiply(a, b)
print(c)  

# c = a / b
c = np.divide(a, b)
print(c)  

lst1 = [
    [1,2],
    [3,4]
]
 
lst2 = [
    [5,6],
    [7,8]
]
a = np.array(lst1)
b = np.array(lst2) 
c = np.dot(a, b)
print(c)

a = np.array([[1,2],[3,4]])
 
s = np.sum(a)
print(s)   

s = np.sum(a, axis=0)
print(s)   
 
s = np.sum(a, axis=1)
print(s)   
 
s = np.prod(a)
print(s)  
   