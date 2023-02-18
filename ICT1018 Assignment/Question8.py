# example, the square root of 2 is as follows:
# 2^1/2 = x,
# 2 = x^2,
# f(x) = x^2-2,
# f'(x) = 2x
# after three iteratios of the newton raphson method, the answer is very accurate. Hence only three iterations are needed.

#newton raphson method: xn+1 = xn - f(xn)/f'(xn)
#the function for the square root is: f(x) = x^2-c, where c is the number in question

c = int(input("Please enter a number to calculate its square root: ")) #number used for prime algorithm

x= c/2 # is a our starting point for the approximation

flag  = 0

if x < 0:
    flag = 1
    print("The number is invalid")
else:
    while flag == 0:
        xO = x
        f1 = (x*x)-int(c)
        f2 = 2*x
        x = x - f1/f2

        #difference is negligible, square root has been found
        if round(xO) - round(x) == 0:
            flag = 1
    
    print("The square root of ", c, "is: ", x)