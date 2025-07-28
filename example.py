import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 2))
identity = np.eye(3)
random_arr = np.random.rand(3, 3)


print("arr1:\n", arr1)
print("arr2:\n", arr2)
print("zeros:\n", zeros)
print("ones:\n", ones)
print("identity:\n", identity)
print("random_arr:\n", random_arr)


print("\nProperties of arr2:")
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)
print("Dimensions:", arr2.ndim)
