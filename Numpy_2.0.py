# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:25:55 2020

@author: adars
"""


#NUMPY PRACTICE

#What is NumPy?
#NumPy is a python library used for working with arrays.

#It also has functions for working in domain of linear algebra,
# fourier transform, and matrices.

#NumPy was created in 2005 by Travis Oliphant. 
#It is an open source project and you can use it freely.

#NumPy stands for Numerical Python.

#Why Use NumPy ?
#In Python we have lists that serve the purpose of arrays,
# but they are slow to process.

#NumPy aims to provide an array object that is up to 50x faster that 
#traditional Python lists.

#The array object in NumPy is called ndarray, 
#it provides a lot of supporting functions that make working with
# ndarray very easy.

#Arrays are very frequently used in data science,
# where speed and resources are very important.




#Why is NumPy Faster Than Lists?
#NumPy arrays are stored at one continuous place in memory unlike lists, 
#so processes can access and manipulate them very efficiently.

#This behavior is called locality of reference in computer science.

#This is the main reason why NumPy is faster than lists.
# Also it is optimized to work with latest CPU architectures.

#Which Language is NumPy written in?
#NumPy is a Python library and is written partially in Python, 
#but most of the parts that require fast computation are written in C or C++.



import numpy
import numpy as np

print(np.__version__)

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

she = numpy.array([2,3,4,5,6,7,8,9])
print(she)

her = numpy.array([34,44,45,56,66,67,77,78])
print(her)

arrr = numpy.array([33,44,55,66,77,88,99])
print(arrr)


#creating a rank 1 array

arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
 
# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using "
      "passed tuple:\n", arr)

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)


arr = np.array([[-6,-7,-8,-9,-1.5],
                [23,34,45,56,67],
                [2.1,-4.5,6.7,-8.9,7.8],
                [22,33,44,55,66],
                [2.3,3.4,4.5,5.6,6.7]])
print("Arry with Rank 2: \n", arr)
print("\nArray created using "
      "passed tuple:\n", arr)
print(arr)


#Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)
 
# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

aniket = arr[:3, ::3]
print ("Array with first 3 rows and"
    " alternate columns(0 and 3):\n", sliced_arr)


#Basic Array Operations
#In numpy, arrays allow a wide range of operations which can be performed
# on a particular array or a combination of Arrays. 
#These operation include some basic Mathematical operation as well
# as Unary and Binary operations.

# Python program to demonstrate
# basic operations on single array
import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray sum:\n", a + b)


#ANOTHER EXAMPLE OF BASIC ARRAY OPRATION

c = np.array([[34,45],
             [3.3,-7.7]])

d = np.array([[44.66,77.77],
             [6.7,-9.8]])

#adding 45 to every element
print("Adding 1 to each element:",c + 1,d +1)

#Subtracting 34 from each element
print("\nSubtracting 34 from each element:", c - 34,d - 34)

#Adding two arrays
#Performing Binary operations
print("\nArray sum:\n", c +d)























