import math

#Number Function: Absoulute Value
number = -10
result = math.fabs(number)
print("The Absoulute value of ", number, "is: ", result)

#Power and Logarithmic Functions: Exponentiation
base = 5
exponent = 3
expResult = math.pow(base, exponent)
print(base, " raised to the power of ", exponent, " is equal to ", expResult)

#Trigonometric Function: Sine Function
Angle = 90
triResult = math.sin(math.radians(Angle))
print("The sine of ", Angle, " degrees is approximately ", triResult)

#Angular Conversion Function: Degrees to Radians Conversion
degrees = 180
radResult = math.radians(degrees)
print(degrees, "in radians is", radResult)

#Hyperbolic Function: Hyperbolic Sine Function
x = 2
hyperResult = math.sinh(x)
print("The Hyperbolic sine of", x, "is:", hyperResult)