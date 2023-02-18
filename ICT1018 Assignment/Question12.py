#fibonacci sequence
#1+1 = 2
#1+2 = 3
#2+3 = 5
#3+5 = 8 etc...

def FibonacciSum(x): #x is the number of iterations
    if (x <= 0): #if x is smaller than or equal to zero then the input in invalid and zero is returned
        return 0
  
    sumArray = [0] * (x+1) #creating an empty array of size x+1
    sumArray[0] = 1  #first fibonacci number is one
    sumArray[1] = 1  #second fibonacci number is one
  
    #creating the first sum, i.e. the third position (x = 2)
    sum = sumArray[0] + sumArray[1] 
  
    #calculating the rest of the sum values strating from x = 2 to the end (x+1)
    for i in range(2, x+1):
        sumArray[i] = sumArray[i-1] + sumArray[i-2] #calculating the sum of the previous 2 numbers
        sum = sum + sumArray[i]
         
    return sum #returning the sum
 

n = 5 #is the number of iterations
print("Sum of Fibonacci numbers is : " , FibonacciSum(n)) #printing the final sum