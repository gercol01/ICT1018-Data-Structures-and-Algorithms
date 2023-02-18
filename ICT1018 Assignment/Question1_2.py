import random

#creating two uneven arrays of size greater than 256
arrayA = [None]*260 #array of size 260 
arrayB = [None]*270 #array of size 270

#populating the arrays by integers between 0 and 1024
for x in range(len(arrayA)):
    arrayA[x] = random.randint(0,1024)

for x in range(len(arrayB)):
    arrayB[x] = random.randint(0,1024)

def shellSort(array,n): #shell sort function with arrayA as a parameter
    gap = n//2 #initialising the gap which originaly is half the size of the array i.e. 130

    while gap > 0: #algorithm is repeated till gap is 1
        for i in range (gap,n): #starting value is gap and ends at the end of the array
            temp = array[i] #temp holds the value in question
            j = i
            while j>= gap and array[j-gap] > temp: #if j is greater or equal to the gap and the number (arrayA[j-gap]) is greater than temp, then a swap occurs
                #swapping the contents
                array[j] = array[j-gap]
                j=j-gap
            array[j] = temp #swapping
        gap = gap//2 #gap is divided by two and the algrithm is repeated till needed

print('Array before Sorting:')
print(arrayA)
shellSort(arrayA,len(arrayA))#Sorting array a by SHELL SORT
print('Array after Sorting:')
print(arrayA)

def median(array, low, high): #function used to find the median of the array, used for pivot
    arrayM = [] #stores the values randomly chosen to be used for the median
    for x in range(0, 11): #randomly selecting an odd number of values from the array, for this case 11 numbers are being selected.
        arrayM.append(array[random.randint(low,high)])
    index1 = 5 #position of the median
    return sorted(arrayM)[index1] #returns the median value

def qSort(array, low, high):
    if len(array) == 1:
        return array
    if (low < high):
        PivotPosition = partition(array,low,high)
        qSort(array, low, PivotPosition-1)
        qSort(array, PivotPosition+1, high)
    
def partition(array, first, last):
    pivot = median(array,first,last)
    for x in range(first,last+1):
        if array[x] == pivot:
            index2 = x
            break
    
    #moves the median to the front
    temp1 = pivot
    array[index2] = array[first]
    array[first] = temp1

    f = first
    l = last
    while f < l:
        while (f < last ) and (pivot>=array[f]):#'f' searches the array for a number greater than the pivot
            f = f+1
        while (pivot < array[l]):#'l' searches the array for a number smaller than the pivot
            l = l-1
        if(f < l):#checks for overlap
            #swaps larger and smaller numbers
            temp2 = array[f]
            array[f] = array[l]
            array[l] = temp2
    
    #swaps pivot (which is initialy stored in the first position) with a smaller number
    temp3 = array[first]
    array[first] = array[l]
    array[l] = temp3      
    return l #returns the position of the pivot, which will be used to partition the array into sub arrays

print('Array before Sorting:')
print(arrayB)
qSort(arrayB, 0, len(arrayB)-1) #Sorting array B by QUICK SORT
print('Array after Sorting:')
print(arrayB)

def mergeArrays(array1, array2, array3):
    i = 0
    j = 0
    k = 0

    #Traverse both arrays
    while i < len(array1) and j < len(array2):
        # Check if current element of first array is smaller than current element of second array. 
        # If yes, store first array element and increment first array index. 
        # Otherwise do same with second array
        if array1[i] < array2[j]:
            array3[k] = array1[i]
            k = k + 1
            i = i + 1
        else:
            array3[k] = array2[j]
            k = k + 1
            j = j + 1
 
    # Store remaining elements
    # of first array
    while i < len(array1):
        array3[k] = array1[i]
        k = k + 1
        i = i + 1
 
    # Store remaining elements
    # of second array
    while j < len(array2):
        array3[k] = array2[j]
        k = k + 1
        j = j + 1
    
#creating an array the combined size of arrayA and arrayB
arrayC = [None] * (len(arrayA)+len(arrayB))
mergeArrays(arrayA, arrayB, arrayC)
print("ArrayC after merging arrayA and arrayB") #printing sorted array
print(arrayC)#printing sorted array