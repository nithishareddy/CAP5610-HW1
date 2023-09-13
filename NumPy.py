import numpy
from numpy.linalg import norm

## this file is for question 2
#Please write a Python code to calculate Correlation, Cosine similarity, and Euclidean distance using NumPy. The input will be two randomly generated or given vectors.  

#Read inputs from terminal
inputArr1= list(map(int,input("Enter first array (eg: 1 2 0):").split()))
inputArr2= list(map(int,input("Enter second array (eg: 5 6 3):").split()))
inputArr1 = numpy.asarray(inputArr1)
inputArr2 = numpy.asarray(inputArr2)
print("first vector:",inputArr1)
print("second vector:",inputArr2)

# finding euclid distance
euclid_dist = numpy.sqrt(numpy.sum(numpy.square(inputArr1 - inputArr2)))
print("euclid distance:",euclid_dist)

# compute cosine similarity
cosine_sim = numpy.dot(inputArr1,inputArr2)/(norm(inputArr1)*norm(inputArr2))
print("Cosine Similarity:", cosine_sim)

# compute correlation
correlation = numpy.corrcoef(inputArr1,inputArr2)
print("correlation:",correlation[0,1]) # print correlation coefficient of x with y