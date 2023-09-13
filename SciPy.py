
from scipy.spatial.distance import cosine
from scipy.spatial import distance
from scipy.stats import pearsonr
import pandas as pd

# this file contains code for question 3 
#Are Correlation, Cosine similarity, and Euclidean distance functions defined in SciPy AND Pandas? If there are, please give another version of the above code by calling them directly. 

#Read inputs from terminal
inputArr1= list(map(int,input("Enter first array (eg: 1 2 0):").split()))
inputArr2= list(map(int,input("Enter second array (eg: 5 6 3):").split()))
inputArr1 = pd.Series(inputArr1)
inputArr2 = pd.Series(inputArr2)
print("first vector:",inputArr1)
print("second vector:",inputArr2)

#euclid distance
euclid_distance = distance.euclidean(inputArr1,inputArr2)
print("euclid distance : ",euclid_distance)


#cosine similarity
cosine_sim = 1-cosine(inputArr1,inputArr2)
print("cosine similarity: ",cosine_sim)


#correlation computation
correlation = pearsonr(inputArr1,inputArr2)
print("correlation : ",correlation[0]," ( pvalue : ",correlation[1],")")

