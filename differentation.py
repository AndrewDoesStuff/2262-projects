from math import sin
'''
# This program computes the forward and backward difference formulas,
# as well as the Lagrange basis and undetermined coefficients.
#
# CSC 2262 Programming Project No ???
#
# @author Andrew Hannie
# @since 11/6/2020
'''

def main():
    x = 2
    values = [0.2, 0.1, 0.05, 0.025, 0.0125]
    forward = []
    backward = []
    lagrange = []
    undetermined = []
    for h in values:
        forward.append(forwardm(x, h))
        backward.append(backwardm(x, h))
        lagrange.append(lagrangem(x, h))
        undetermined.append(undeterminedm(x, h))
    print("{:<30}{:<30}{:<30}{:<30}{:<30}".format("h", "FDF", "BDF", "LB", "UC"))
    for i in range(0, len(values)):
        print("{:<30}{:<30}{:<30}{:<30}{:<30}".format(values[i],forward[i], backward[i], lagrange[i], undetermined[i]))        

'''
# This method returns the function for the backwards difference formula.
#
# method: backwardm
#
# return type: float
#
# parameters:
#     x   [float]     the x0 value that stays the same
#     h   [float]     the given values in the list.
'''
def backwardm(x, h):
    return (f(x) - f(x - h)) / h
'''
# This method returns the function for the forward difference formula.
#
# method: forwardm
#
# return type: float
#
# parameters:
#     x   [float]     the x0 value that stays the same
#     h   [float]     the given values in the list.
'''
def forwardm(x, h):
    return (f(x + h) - f(x)) / h
'''
# This method returns the function for the lagrange basis formula.
#
# method: backwardm
#
# return type: float
#
# parameters:
#     x   [float]     the x0 value that stays the same
#     h   [float]     the given values in the list.
'''
def lagrangem(x, h):
    return ((f(x + h)) - (f(x - h))) / (2 * h)
'''
# This method returns the function for the undetermined coefficients formula.
#
# method: undeterminedm
#
# return type: float
#
# parameters:
#     x   [float]     the x0 value that stays the same
#     h   [float]     the given values in the list.
'''    
def undeterminedm(x, h):
    return ((f(x + h)) - (2 * f(x)) + (f(x - h))) / h ** 2
'''
# This method returns the original function given in the beginning of the assignment.
#
# method: f
#
# return type: float
#
# parameters:
#     x    [float]     whatever value being passed that the function is to be run on.
'''
def f(x):
    # return (1 + (x ** 2)) ** -1
    return sin(x)
main()