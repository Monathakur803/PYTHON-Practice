import numpy as np

# Create a 3x3 array filled with the value 10.1
array1 = np.full((3, 3), 10.1)

# Create a 3x3 array filled with the integer value 55
array2 = np.full((3, 3), 55, dtype=int)

# Create a 3x3 array filled with the boolean value True
array3 = np.full((3, 3), True, dtype=bool)

# Print the arrays
print(array1)
print(array2)
print(array3)