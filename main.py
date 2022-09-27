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





'''
outfile = open(job[0] + '/' + output, 'wb');

dist_min = float(job[5]);
dist_max = float(job[6]);

dists = [];

for node in nodes:

  shortest_distance = 1000.0;
  shortest_data = 0.0;

  for entry in data:
    dist = math.sqrt((node[1] - entry[0])**2 + (node[2] - entry[1])**2 + (node[3] - entry[2])**2);
    if (dist_min <= dist <= dist_max) and (dist < shortest_distance):
      shortest_distance = dist;
      shortest_data = entry[3];

  outfile.write(node[0] + ', ' + str('%10.5f' % shortest_data + '\n'));

outfile.close()

'''
'''
counter=0
with open("cropped_C2M_within.txt") as f:
    while True:
        data = f.read()
        if not data:
            print(counter)
            break
        print(data[1])
        counter+=1


'''