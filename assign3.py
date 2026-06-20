#- -------------------------------------------------------------------------
# PHY1038 Assignment 3 - Finite difference methods
# URN 6868959
# 12/03/25
#---------------------------------------------------------------------------
#imports
import module_URN6868959 as mod
import scipy.integrate as spi

x = float(input("enter the value for x: "))
h = float(input("enter the value for h: "))

dfor = mod.dfor(x , h)
dcen = mod.dcen(x , h)
derivative = mod.exact_derivative(x)

delta_dfor = (dfor - derivative)
delta_dcen = (dcen - derivative)

print("\nThe value of the derivative from the forward difference method = " , dfor)
print("The value of the derivative from the centred difference method = " , dcen)
print("The exact value for the first derivative f(x) = " , derivative)
print("The error in the forward difference method = " , delta_dfor)
print("The error in the centred difference method = " , delta_dcen)

#The smaller the value of h the more presice the drivative

d2cen = mod.d2cen(x , h)
exact_second_derivative = mod.exact_second_derivative(x)

print("\nThe value of the second derivative from the centred difference method = " , d2cen)
print("The exact value for the second derivative f(x) = " , exact_second_derivative)

#Simarley to the first derivative the smaller the value of h the more precise the value for the second derivative

a = float(input("\nInput the lower bound a: "))
b = float(input("Input the upper bound b: "))
N = int(input("Input the number of bins N (needs to be even for simpsons rule): "))

exact_intergral = mod.exact_intergral(a , b)
print("The exact value of the intergral between a nad b = " , exact_intergral)

itrap = mod.functioni(a , b , N)
print("\nThe value of the intergral between a and b using the trapezium rule = " , itrap)

errortrap = (exact_intergral - itrap)
print("The error for the trapezeum rule = " , errortrap)

isimp = mod.isimp(a , b , N)
print("\nThe value of the intergral between a and b using the simpson's rule = " , isimp)

errorsimp = (exact_intergral - isimp)
print("The error for the simpsons rule = " , errorsimp)

I = spi.quad(mod.functionf , a , b)
print("\nThe value of the intergral between a and b using SciPy = " , I[0])

errorspisimp = (I[0] - isimp)
print("The error for the trapezeum rule, using SciPy = " , errorspisimp)



