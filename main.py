# Libraries and dependencies
# ---------------------------------------
import numpy as np
from scipy.spatial import KDTree


# Loading Original Point Cloud and Sampled Mesh Data
# -------------------------------------------------- 
counter=0
original = []
with open("original.txt") as infile:
    for line in infile:
        print(line)
        original.append(line)
        counter+=1

print(counter)
print("The original data is ", original)
print(original[2])


# Format the line by line data into 3D vectors
# The primary key for both list/vector/array must be maintained
# To later retrieve the data from original files for angle computation
# --------------------------------------------------------------------


# Test data using numpy arrays
# -----------------------------------------
data= np.random.randint(10, size=(5, 3))
sample= np.random.randint(10, size=(5, 3))
print("Test data ", data)
print("Sample data ", sample)


# Initializing KD Tree
# -----------------------------------------
kdtree=KDTree(data)


dist,points=kdtree.query(sample,2)
print("The distance for nearest 2 neighbors are ", dist)
print("The nearest 2 neighbor points are ", points)



