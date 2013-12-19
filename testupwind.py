import numpy as np
import math

Array = np.array([1,2,3,4,5,6,7])

print Array
print Array[1:len(Array)]

for i in Array[1:5]:
    value = Array[i] + Array[i-1]
    print value
    
#need to find the type of a len()

if type(Array) != int:
    print "type(Array) != int:"

k = 0
while(k < len(Array) + 1):
    if k == len(Array):
        gridlength = k
        print gridlength
    k = k + 1

if type(gridlength) == int:
    print "type(gridlength) is an integer"