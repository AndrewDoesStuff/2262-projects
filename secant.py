import math
'''
This method is the secant method.

method: Secant Method

return type: double technically but this is python so anything goes

parameters:
    x0 [int / double] First parameter passed to the secant method.
    x1 [int / double] Second parameter passed to the secant method

@author Andrew Hannie
@since 9/25/2020

'''
def SecantMethod(x0, x1):
    # Conversion to float just in case something weird happens
    x0 = float(x0) 
    x1 = float(x1)
    return x1 - f(x1) / ((f(x1) - f(x0)) / ((x1) - x0)) # Do the secant method
'''
This method is just the given function that we can use inside the secant method 
and outside the secant method.

method: f

return type: double

parameters:
    x [double] The number that the function is being used upon.

@author Andrew Hannie
@since 9/25/2020

'''
def f(x): 
    return math.cos(x) - x

'''

This is the main method, that runs all of the requested calculations and outputs them to the console in a nicely 
formatted table.

method: main

return type: void

@author Andrew Hannie
@since 9/25/2020

'''
def main():
    arr = [] # Array of requested calculations
    arr.append(2.0) # First parameter
    arr.append(1.0) # Second parameter
    print("{:<8} {:^8} {:^24} {:>10}".format("n", "xn", "f(xn)", "xn - x(n-1)")) # table formatting
    for i in range(0, 6):  # writes all of the calculations to the list and formats them
        if i < 2: # catches impossible calculations
            if i == 0:
                print("{:<8} {:^8} {:^30}".format(i, arr[i], f(arr[i])))
            elif i == 1:
                print("{:<8} {:^8} {:^30} {:<10}".format(i, arr[i], f(arr[i]), arr[i] - arr[i-1]))
            continue
        # After the impossible calculations have been caught, the secant method is performed on the rest of the array list.
        else:
            arr.append(SecantMethod(arr[i-1], arr[i-2]))
            print("{:<8} {:^8} {:^16} {:<10}".format(i, arr[i], f(arr[i]), arr[i] - arr[i-1]))
main() # runs the program :)
