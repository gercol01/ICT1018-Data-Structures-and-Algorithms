import random

"""arrayd = [None]*20 #array of size 20

#creating an array with random numbers from 0 - 20
for x in range(len(arrayd)):
    arrayd[x] = random.randint(0, 20)"""

arrayd = [1,2,3,23,1]
    
print(arrayd) #showing the user the array in question

arrayn = [] #array which has no duplicates

if len(arrayd) > 0:
    arrayn.append(arrayd[0])#adding the first number

#traversing the whole array starting from the second number
for x in range(1,len(arrayd)):
    flag = 0
    for y in range(len(arrayn)):
        if arrayn[y] == arrayd[x]: #if the number already exists
            flag = 1
            break
        if arrayd[x] < arrayn[0]: #if the number in question is smaller than the smallest number in the unique array, the number is added since the array is sorted
            break
    if flag == 0:
        arrayn.append(arrayd[x])
        arrayn = sorted(arrayn)
    else:
        print(arrayd[x], " is a duplicate.")