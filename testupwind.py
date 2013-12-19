import numpy as np
import math

Array = np.array([1,2,3,4,5,6,7])

print Array
print Array[1:len(Array)]

for i in Array[1:5]:
    value = Array[i] + Array[i-1]
    print value