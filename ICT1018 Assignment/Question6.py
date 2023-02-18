"""def prime(number):
    e = round(number/2) #rounding the number
    flag = 0 #used to show if a number is a prime number or not
    for x in range(2, e+1): #checking numbers which are greater than 'e+1' is unnecessary
        if x != 2:
            x=x+1 #traversing odd numbers only as even numbers are all divisable by 2

        if number % x == 0: #checking if the number is a prime or not
            flag = 1
            break
        
    
    if flag == 0:
        print("the number" , number, " is a prime number")
    else:
        print("the number" , number, " is not a prime number")

a = input("Please enter a number: ") #number used for prime algorithm
prime(int(a))"""

array1 = [2,3,4,5,6,7,8,9,10] #empty array

"""for x in range(2,40+1): #adding the numbers 2 to 40
    array1.append(x)"""

print("The array in question is: ", array1)

#Sieve of Eratosthenes algorithm to find prime numbers
def SieveofEratosthenes(array):
    for i in range(len(array)): #traversing the array
        for j in range(i+1,len(array)):
            if array[j] != 0 and array[i] != 0:
                if array[j] % array[i] == 0:
                    array[j] = 0 #'0' means that it is not a prime
    
    print("The prime numbers are")
    for k in range(len(array)):
        if array[k] != 0: #a zero in the array represents a non prime number
            print ("The number: ", array[k], " is a prime number")
            
SieveofEratosthenes(array1)