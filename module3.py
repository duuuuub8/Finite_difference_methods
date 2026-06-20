#---------------------------------------------------------------------------
# PHY1038 Assignment 3 - Finite difference methods
# URN 6868959
# 12/03/25
#---------------------------------------------------------------------------
#imports
import math

#returns the falue of the function
def functionf(x):
    y = (1 / ((x ** 2) + (3 * x) + 2))
    
    return y


#calls the functionf(x) to find an estamate for the first
#derivative of f(x) using the forward differnce method.
def dfor(x , h):
    y = ((functionf(x + h) - functionf(x)) / h)
    
    return y


#calls the functionf(x) to find an estamate for the first 
#derivative of f(x) using the centred differnce method.
def dcen(x , h):
    y = ((functionf(x + (h / 2)) - functionf(x - (h / 2))) / h)
    
    return y


#finds the exact first derivative for the function f(x)
def exact_derivative(x):
    y = (-1 * (((2 * x) +3) * ((functionf(x) ** 2))))
    
    return y


#finds an estamate for the second derivative by calling dcen(x , h)
def d2cen(x , h):
    y = ((dcen((x + (h / 2)) , h) - dcen((x - (h / 2)) , h)) / h)
    
    return y


#finds the exact derivative of f(x)
def exact_second_derivative(x):
    y = ((2 * (((2 * x) + 3) ** 2) * (functionf(x) ** 3)) - (2 * (functionf(x) ** 2)))
    
    return y



def functioni(a , b , N):
    #empty list to add the elements of the sum to
    list1 = []
    
    #finds the value of h
    h = ((b - a) / N)
    
    #finds the value of the sum at each value between 1 and N-1 and adds it to the list
    for j in range(1 , N):
        list1.append(functionf(a + (j * h)))
        
    sigma = sum(list1) #finds the sum of the values in the list
    
    #finds the value of the intergral
    y = (((h / 2) * (functionf(a) + functionf(b))) + (h * sigma))
    
    return y


#finds the exact value of the intergral of f(x) between a and b
def exact_intergral(a , b):
    y = (math.log((b + 1) / (b + 2)) - math.log((a + 1) / (a + 2)))
    
    return y


def isimp(a , b , N):
    #empty lists to add the elements of the sums to
    list1 = []
    list2 = []
    
    #finds the value of h
    h = ((b - a) / N)
    
    #finds the value of the sum at every other value between 1 and N-1 and adds it to the list
    for j in range(1 , N , 2):
        list1.append(functionf(a + (j * h)))
    
    #finds the value of the sum at every other value between 2 and N-2 and adds it to the list
    for j in range(2 , N - 1 , 2):
        list2.append(functionf(a + (j * h)))
    
    #find sthe sums of the 2 lists
    sigma1 = sum(list1)
    sigma2 = sum(list2)
    
    #finds the value of the intergral
    y = ((h / 3) * (functionf(a) + functionf(b) + (4 * sigma1) + (2 * sigma2)))
    
    return y





