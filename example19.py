import numpy as np
arr_1 = np.array([1, 2, 3])
arr_2 = np.expand_dims(arr_1, axis = 0)
arr_3 = np.expand_dims(arr_2, axis = (0,2,4))
print(arr_1, arr_2.shape)
print(arr_2, arr_2.shape)
print(arr_3, arr_3.shape)