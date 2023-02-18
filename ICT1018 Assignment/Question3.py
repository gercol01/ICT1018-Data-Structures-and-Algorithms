import random #used to create random numbers

"""array1 = [None]*8 #array of size 8

#populating the array by integers between 0 and 30 (included)
for x in range(len(array1)):
    array1[x] = random.randint(0,30)"""

array1 = [2,5,3,2,1,2]

#empty array to store the extremes of array1, the maximum ammount of extremes in an array is the length - 2 (first and last numbers are excluded)
arrayE = []

#algorithm that writes the extreme points of an array
def extremes(arrayC, arraye):
    #flag used to check if the array contains extreme points
    flag = False

    for x in range (1,len(arrayC)-1): #the ends of the array cannot be extremes, hence they are excluded
        if arrayC[x] > arrayC[x-1] and arrayC[x] > arrayC[x+1]: #if the value is greater than its neighbours
            #adding the extreme value to the array of extremes
            arraye.append(arrayC[x])
            flag = True
        if arrayC[x] < arrayC[x-1] and arrayC[x] < arrayC[x+1]: #if the value is smaller than its neighbours
            #adding the extreme value to the array of extremes
            arraye.append(arrayC[x])
            flag = True

    if flag == False: #if there are no extreme values in the entire array, "SORTED" is printed
        print("SORTED")

print("Original array: ")
print(array1)
extremes(array1,arrayE)
print("Array of extreme values: ")
print(arrayE)

#"Do you agree that an array has no extreme points if and only if it is sorted?" I do not agree as an array which is made up of five '1's has no extremes yet it is not sorted. 
# Omitting this case, then, I do agree with the above statement.