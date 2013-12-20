import numpy as np
import math

Array = np.array([1,2,3,4,5,6,7])
newArray = np.zeros(len(Array))
print Array, newArray
#print Array[1:len(Array)]

#for i in Array[1:5]:
#    value = Array[i] + Array[i-1]
#    print value

#if type(Array) != int:
#    print "type(Array) != int:"
#
k = 0
while(k < len(Array) - 1):
    k = k + 1
    newArray[k] = Array[k] + (Array[k-1] + Array[k])
    print "k = ", k
newArray[0] = Array[0] + (Array[len(Array)-1] - Array[0])
print "newArray = ", newArray

#if type(gridlength) == int:
#    print "type(gridlength) is an integer"
#
#newArray = np.zeros((1, len(Array)))
#print newArray
#print Array[0]
#j = 0
#for j in Array[1:len(Array)-1]:
#    num = j
#    print Array[num]
#    newArray[j] = Array[j] + (Array[j-1] - Array[j])#IndexError: list assignment index out of bounds
#newArray[0] = Array[0] + (Array[len(Array)-1] - Array[0])
#print newArray

#it appears that although the range is appropriate, there is no count