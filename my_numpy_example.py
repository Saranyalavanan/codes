import numpy as np
arr1 = np.array([3,6,9,12,15])
arr2 = np.array([[2,4,6], [8,10,12], [15,18,21]])
zeros = np.zeros((2,2))
ones = np.ones((3,3))
identity = np.eye(3)
random_arr = np.random.rand(2,2)
def  properties(arr):
    print("Array:\n", arr)
    print("Shape:", arr.shape)
    print("Size:", arr.size)
    print("Datatype:", arr.dtype)
    print("Dimensions:", arr.ndim)
    print()
x = int(input("Enter a number : "))
if x == 1:
   properties(arr1)
elif x == 2:
   properties(arr2)
elif x == 3:
   properties(zeros)
elif x == 4:
   properties(ones)
elif x == 5:
   properties(identity)
elif x == 6:
   properties(random_arr)
  
