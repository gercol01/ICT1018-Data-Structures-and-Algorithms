#maclaurin series expansion for sin(x) is given by
# sin(x) = x - (x^3)/3! + (x^5)/5! etc....
# cos(x) = 1 - (x^2)/2! + (x^4)/4! etc....

import math

def sin(angle):
    return angle - (angle*angle*angle)/6 + (angle*angle*angle*angle*angle)/120

def cos(angle):
    return 1 - (angle*angle)/2 + (angle*angle*angle*angle)/24

#calling the respective functions
c = int(input ("Please enter a number for the cosine function: "))
print("The answer is: ",cos(math.radians(c))) #turning degrees into radians
s = int(input ("Please enter a number for the sin function: "))
print("The answer is: ",sin(math.radians(s))) #turning degrees into radians