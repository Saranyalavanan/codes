import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)
print(arr1)
print(arr2)
print(zeros)
print(ones)
print(identity)
print(random_arr)

# Array properties
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)
print("Dimensions:", arr2.ndim)
