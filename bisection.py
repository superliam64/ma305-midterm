#!/usr/bin/python3
import math
def bisection(left,right,k=0):
    if(k==50):                 #iterates 50 times to get precision of 15 decimal places
        return (left/2)+(right/2)  #base case
    else:
        if(abs(math.sin(left))>abs(math.sin(right))):           #recursive cases
            return bisection((left/2)+(right/2),right,k+1)          
        else:
            return bisection(left,(left/2)+(right/2),k+1)
print(bisection(3,4))   #starts off looking between 3 and 4
print(math.pi)          #pi acording to math library for comparison