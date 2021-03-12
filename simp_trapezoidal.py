import numpy as np
import math
def trapezoidal(a, b, size):
    subintervals = np.linspace(a, b, size+1)
    subintervals = list(subintervals)
    summation = 0
    for i in subintervals:
        if i == subintervals[0]:
            summation += f(i)
        elif i == subintervals[len(subintervals) - 1]:
            summation += f(i)
        else:
            summation += 2 * f(i)
    delta = (b - a) / size
    return (delta / 2) * summation


def simpson(a, b, size):
    subintervals = np.linspace(a, b, size + 1)
    subintervals = list(subintervals)
    summation = 0
    for i in range(len(subintervals)):
        if i == 0:
            summation += f(subintervals[i])
        elif i == len(subintervals) - 1:
            summation += subintervals[i]
        elif i % 2 == 1: # Odd number
            summation += 4 * f(subintervals[i])
        elif i % 2 == 0: # Even Number
            summation += 2 * f(subintervals[i])
    delta = (b - a) / size
    return (delta / 3) * summation

def f(x):
    return math.log(x, math.e)

def main():
    a = 1
    b = 3
    size = 512
    print("Trapezoidal Rule: T" + str(size) + "(f) = " + str(trapezoidal(a, b, size)))
    print("Simpson Rule: T" + str(size) + "(f) = " +  str(simpson(a, b, size)))
main()