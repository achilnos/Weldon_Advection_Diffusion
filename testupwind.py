import numpy as np
import math

Array = np.array([1,2,3,4,5,6,7])

print Array
print Array[1:len(Array)]

for i in Array[1:5]:
    value = Array[i] + Array[i-1]
    print value

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

newArray = np.zeros((1, len(Array)))
print newArray
print Array[0]
j = 0
for j in Array[1:6]:
    num = j
    print Array[num]
    #newArray[j] = Array[j] + (Array[j-1] - Array[j])#IndexError: list assignment index out of bounds
#newArray[0] = Array[0] + (Array[len(Array)] - Array[0])
#print newgrid

#it appears that the obj[] command will not function unless the input is an integer, not even a variable whose value is an integer will work. 