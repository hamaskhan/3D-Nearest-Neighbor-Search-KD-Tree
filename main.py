# Libraries and dependencies
# ---------------------------------------
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

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


# Random Test data
# --------------------------------------------------------------------
'''
data= np.random.randint(10, size=(5, 3))
sample= np.random.randint(10, size=(5, 3))
print("Test data ", data)
print("Sample data ", sample)
'''

# Specific Test data
# --------------------------------------------------------------------

test_ref=np.array([[1,1,1], [-1,-1,-1]])
test_sample=np.array([[3,3,3],[4,4,4],[0,0,0], [-3,-3,-3],[-4,-4,-4]])
#test_sample=np.array([[3,4,5],[-1,0,9],[10,3,0], [-3,0,-3],[-4,-41,45]])

print("These are the reference test points ", test_ref)
print("These are the sample test points ", test_sample)


# Initializing KD Tree and nearest neighbor return
# --------------------------------------------------------------------
kdtree=KDTree(test_sample)


dist,points=kdtree.query(test_ref,2)
print("The distance for nearest 2 neighbors are ", dist)
print("The nearest 2 neighbor point indices are ", points)
nearest = test_sample[points]
print("The nearest 2 neighbor points are ", nearest)

# 3D plotting of original, sampled and nearest points
# --------------------------------------------------------------------

fig=plt.figure()
ax = plt.axes(projection='3d')

#print("X axis of sample test points are ",test_sample[:,0])
#print("Y axis of sample test points are ",test_sample[:,1])
#print("Z axis of sample test points are ",test_sample[:,2])


ax.scatter3D(test_ref[:,0], test_ref[:,1], test_ref[:,2], label="Original Points")
ax.scatter3D(test_sample[:,0], test_sample[:,1], test_sample[:,2], label="Sample Points", marker="_")

# Select for which points you want to show neighbors
# ---------------------------------------------------------------------
ax.scatter3D(nearest[0][:,0], nearest[0][:,1], nearest[0][:,2], label="Nearest 2 Points for [1 1 1]", marker="x")
#ax.scatter3D(nearest[:, :, 0], nearest[:, :, 1], nearest[:, :, 2], label="Nearest 2 Points for all original points", marker="x")


plt.title("3D scatter plot for Nearest Neighbor")
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.legend(loc="upper right")
plt.show()