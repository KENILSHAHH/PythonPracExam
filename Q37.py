import numpy as np

array_data = np.arange(0,16).reshape((4, 4))
print("Original array:")
print(array_data)
print("\nExtracted data: Second row")
print(array_data[1,0:2])

