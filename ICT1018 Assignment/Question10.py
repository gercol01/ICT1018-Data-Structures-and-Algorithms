def Maximum(A,n):
    #the function is repeated until the length of the array (n) is one.
    if(n==1): #if the length of the array is one, that only value is the maximum value of the array
        return A[0]
    
    else:
        before = Maximum(A, n-1) #calling the function again with the length being reduced by one, this is repeated until the left most numer is selected
        current = A[n-1] #the current number in question                                                     
        if before > current: #if the number before is greater than the number in question, that becomes the maximum                                         
            return before                                                   
        else: #else if the number in question is greater, that is the maximum                                                           
            return current

#Testing code
A = [1,-4,54,3]
n = len(A) #the length of the array
if n > 0:
    print("The maximum number is ", Maximum(A, n)) #calling the method
else:
    print("invalid length")