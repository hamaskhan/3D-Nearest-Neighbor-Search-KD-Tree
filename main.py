# Libraries and dependencies
# ---------------------------------------
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

'''
# The format of data in the text file is as below

//  X  ;   Y   ;   Z  ;Value;    Nx  ;     Ny  ;    Nz
385.888;145.156;44.359;1.504;0.272890;-0.422294;0.864407
409.526;176.741;22.387;0.020;0.956552;-0.021037;0.290802
388.059;145.798;42.530;0.953;0.426310;-0.423093;0.799533
398.934;167.566;38.444;1.196;0.734180;-0.292712;0.612617
'''


# Data loading and pre-processing
# The primary key for both (original & post processing) list/vector/array must be maintained
# To later retrieve the data from original files
# Data is loaded in to an NxM matrix using the delimiter arguments
# ------------------------------------------------------------
original = np.genfromtxt("original.txt", skip_header=1, dtype=str, delimiter=';')
sampled = np.genfromtxt("sampled.txt", skip_header=1, dtype=str, delimiter=';')
print(original)
print(sampled)

# Get a specific column for all rows. Similarly get a specific row for all columns
# print(original[:,6])
# print(original[1,:])

# Convert string matrix to int
original2d=original.astype(np.float32)
sampled2d=sampled.astype(np.float32)

# Select first three columns for all rows to get only x, y,z data
originalxyz=original2d[:, [0, 1,2]]
sampledxyz=sampled2d[:, [0, 1,2]]

print(originalxyz)
print(sampledxyz)

'''
# Random Test data
# --------------------------------------------------------------------

data= np.random.randint(10, size=(5, 3))
sample= np.random.randint(10, size=(5, 3))
print("Test data ", data)
print("Sample data ", sample)


# Specific Test data
# --------------------------------------------------------------------

test_ref=np.array([[1,1,1], [-1,-1,-1]])
test_sample=np.array([[3,3,3],[4,4,4],[0,0,0], [-3,-3,-3],[-4,-4,-4]])
#test_sample=np.array([[3,4,5],[-1,0,9],[10,3,0], [-3,0,-3],[-4,-41,45]])

print("These are the reference test points ", test_ref)
print("These are the sample test points ", test_sample)
'''

# Initializing KD Tree and nearest neighbor return
# --------------------------------------------------------------------
kdtree=KDTree(sampledxyz)


dist,points=kdtree.query(originalxyz,2)
print("The distance for nearest 2 neighbors are ", dist)
print("The nearest 2 neighbor point indices are ", points)
nearest = sampledxyz[points]
print("The nearest 2 neighbor points are ", nearest)

# 3D plotting of original, sampled and nearest points
# --------------------------------------------------------------------

fig=plt.figure()
ax = plt.axes(projection='3d')

#print("X axis of sample test points are ",test_sample[:,0])
#print("Y axis of sample test points are ",test_sample[:,1])
#print("Z axis of sample test points are ",test_sample[:,2])


ax.scatter3D(originalxyz[:,0], originalxyz[:,1], originalxyz[:,2], label="Original Points")
ax.scatter3D(sampledxyz[:,0], sampledxyz[:,1], sampledxyz[:,2], label="Sample Points", marker="_")

# Select for which points you want to show neighbors
# ---------------------------------------------------------------------
#ax.scatter3D(nearest[0][:,0], nearest[0][:,1], nearest[0][:,2], label="Nearest 2 Points for first original point at index[0,0,0]", marker="x")
ax.scatter3D(nearest[:, :, 0], nearest[:, :, 1], nearest[:, :, 2], label="Nearest 2 Points for all original points", marker="x")


plt.title("3D scatter plot for Nearest Neighbor")
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.legend(loc="upper right")
plt.show()
