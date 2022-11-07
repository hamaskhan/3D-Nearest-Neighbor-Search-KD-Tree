# Author: Muhammad Hamas Khan
# Please add this reference if you want to use part of this code:  https://github.com/hamaskhan
# Email: m.hamaskhan@gmail.com
# ---------------------------------------------------------------------------------------------

# Libraries and dependencies
# ------------------------------------------------------
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

# Suppresing scientific notation for easy readability
np.set_printoptions(suppress=True)

# 3D plotting of points and reference cloud
# --------------------------------------------------------------------
def plot_3D():
    fig=plt.figure()
    ax = plt.axes(projection='3d')

    #print("X axis of sample test points are ",test_sample[:,0])
    #print("Y axis of sample test points are ",test_sample[:,1])
    #print("Z axis of sample test points are ",test_sample[:,2])

    ax.scatter3D(pointsxyz[:,0], pointsxyz[:,1], pointsxyz[:,2], label="Points", marker=".")
    ax.scatter3D(referencexyz[:,0], referencexyz[:,1], referencexyz[:,2], label="Reference Cloud Points", marker=".")

    # Select for which points you want to show neighbors
    # ---------------------------------------------------------------------
    ax.scatter3D(nearest[0][:,0], nearest[0][:,1], nearest[0][:,2], label="Nearest 2 Points for point at index[0,0,0]", marker="x")

    # Uncomment below line to see nearest neighbors for all the points
    #ax.scatter3D(nearest[:, :, 0], nearest[:, :, 1], nearest[:, :, 2], label="Nearest 2 Reference Points for all the points", marker="x")

    plt.title("3D scatter plot for Nearest Neighbors")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":

    # Data loading and pre-processing
    # Data is loaded in to an NxM matrix using the delimiter arguments
    # ------------------------------------------------------------
    print("\nLoading Points")
    points = np.genfromtxt("points.txt", skip_header=1, dtype=str, delimiter=';') #Open3D File IO can also be used
    reference = np.genfromtxt("reference.txt", skip_header=1, dtype=str, delimiter=';') #Open3D File IO can also be used
    print("No. of points are ", points.shape)
    print("Size of reference Point Cloud is ", reference.shape)

    # Convert string matrix to int
    points2d=points.astype(np.float32)
    reference2d=reference.astype(np.float32)

    # Select first three columns for all rows to get only x, y,z data if more columns are present
    pointsxyz=points2d[:, [0, 1,2]]
    referencexyz=reference2d[:, [0, 1,2]]

    print("\nData Loaded")

    # Initializing KD Tree and nearest neighbor return
    # ----------------------------------------------------------------------------
    print("\nInitializing KD Tree with reference point cloud")
    kdtree=KDTree(referencexyz)          # This is the reference point cloud

    dist,pts=kdtree.query(pointsxyz,2)   # Forward data here for the points to be queried for nearest neighbors. 2 represents the nearest 2 neighbor.

    print("The distance for nearest 2 neighbors are ", dist)
    print("The nearest 2 neighbor point indices are ", pts)
    nearest = referencexyz[pts]
    print("The nearest 2 neighbor points are ", nearest)

    plot_3D()