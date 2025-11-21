import numpy as np
arr_1 = np.array([1,2, 3])
arr_2 = arr_1[np.newaxis, :]
arr_3 = arr_2[np.newaxis, :, np.newaxis, :, np.newaxis]
print(arr_1)
print(arr_2, arr_2.shape)
print(arr_3, arr_3.shape)