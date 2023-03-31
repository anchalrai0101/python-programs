#min and max
x= min(55,23,11,65,2,9,4,1,22)
print(x)
y= max(12,85,74,15,2,44,92)
print(y)

#abs()
n= float(input("enter any no-"))
result= abs(n)
print(result)

#pow() 
n= float(input("enter any no-"))
power =int(input("enter the power-"))
result= pow(n,power)
print(result)

#sqrt - sqrt(no)
import math 
num = float(input("enter any no-"))
result= math.sqrt(num)
print(result)

#ceil nd floor
import math
#Round a number upward to its nearest integer
x=math.ceil(1.3)
print(x)
#Round a number downward to its nearest integer
y=math.floor(1.3)
print(y)
#pi
z=math.pi
print(z)
#Euler's number
print(math.e)
# math.inf , -math.inf, math.nan,math.tau = 6.2831
#math.sin()
import math
#return the sine of different values
print(math.sin(0.00))
print(math.sin(math.pi)) #sin180 degrees
print(math.sin(math.pi/2)) #sin90 degrees
print(math.sin(math.radians(90))) #return sine value of 90 degrees
#math.cos,cosh,tan,sinh,tanh,acos,drgrees
print(math.factorial(5)) # 5*4*3*2*1
print(math.fmod(10,3)) #return the remainder of x/y
#x= y=0 valuerror
#y=0 valueerror
# x and y not a number - typeerror
print(math.fsum([2,8,4,1]))

