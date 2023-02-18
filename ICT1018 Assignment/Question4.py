import random

"""array1 = [None]*50 #array of size 50, that stores the initial numbers used to create products

#populating the array by integers between 1 and 1024 (included)
for x in range(len(array1)):
    array1[x] = random.randint(1,1024)"""

array1 = [4,3,2,6]

matrix = [] #empty matrix which will be used to store the products

#traverses  and initialises the matrix 
for i in range (4): #creating the rows of the matrix
    matrix.append([]) #creating an empty sublist in each row

    #traverses the columns of the matrix (50 values in each row, i..e 50 columns of the matrix)
    for j in range (4):
        matrix[i].append(array1[i]*array1[j]) #adds the products to the sublist

"""# An idea of how the matrix would be
array1 = [1, 2, 3, 4, 5, 6]

matrix = [[1, 2, 3, 4 , 5, 6], 
    [2, 4, 6, 8, 10, 12],
    [3, 6, 9, 12, 15, 18],
    [4, 8, 12, 16, 20, 24],
    [5, 10, 15, 20, 25, 30],
    [6, 12, 18, 24, 30, 36]]"""

arrayP = [[]] #creating an empty list of a list to store the already found pairs

#traverses the ROWS of the matrix for pairs
for i in range (4):
    #traverses the COLUMNS of the matrix for pairs
    for a in range (4):
        #traverses the ROWS of the matrix for pairs
        for j in range (4):
            #traverses the COLUMNS of the matrix for pairs
            for b in range (4):
                flag = 0
                if matrix[i][a] == matrix [j][b]:#checking if the products are equal to each other
                    arrayA = [array1[i], array1[a], array1[j], array1[b]]
                    for x in range (len(arrayP)): #checking if the product pairs have already been found
                        if arrayP[x] == sorted(arrayA): # if the product pairs already exist
                            flag = 1
                    
                    if flag == 0:
                        arrayC = [] #empty array used to compare the four numbers which created the two products
                        arrayC.append(array1[i])

                        #traversing the array to see if the number already exists
                        for c in range (len(arrayC)):
                            if array1[j] == arrayC[c]:
                                flag = 1
                                break
                            else:
                                arrayC.append(array1[j])
                                break
                        for c in range (len(arrayC)):
                            if array1[a] == arrayC[c]:
                                flag = 1
                                break
                            else:
                                arrayC.append(array1[a])
                                break
                        for c in range (len(arrayC)):
                            if array1[b] == arrayC[c]:
                                flag = 1
                                break
                            else:
                                arrayC.append(array1[b])
                                break

                    if flag == 0:
                        arrayP.append(sorted(arrayA))     
                        print (array1[i], 'and', array1[a], 'create the same product as', array1[j], 'and', array1[b])
