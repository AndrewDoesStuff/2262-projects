'''
This program computes the values for Newton's Divided Differences Equation

CSC 2262 Programming Project 3

@author Andrew Hannie
@since 9/30/2020
'''

import math


def main():
    xsubi = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2] # requested values
    ivalues = [i for i in range(0, 7)] # for loop that writes requested values
    formulatable = [0 for i in range(0, 7)] # Place where the sin of the values are saved
    for j in range(len(formulatable)):
        formulatable[j] = math.sin(xsubi[j])
    Di = divideddifference(formulatable, xsubi)
    print("{:<10} {:<20} {:<30} {:<40}".format("i", "xi", "sin(xi)", "Di"))
    for k in range(len(formulatable)): # list for formatting
        if k == len(formulatable) - 1: 
            print("{:<10} {:<20} {:<30}".format(str(ivalues[k]), str(xsubi[k]), str(formulatable[k])))
        else:
            print("{:<10} {:<20} {:<30} {:<40}".format(str(ivalues[k]), str(xsubi[k]), str(formulatable[k]), str(Di[k])))
    print("\n\n")
    inter1 = p(xsubi, 0.1) # interpolation 1
    inter3 = p(xsubi, 0.3) # interpolation 2
    inter5 = p(xsubi, 0.5) # interpolation 3
    print("{:<10} {:<20} {:<30} {:<40}".format("i", "Pn(0.1)", "Pn(0.3)", "Pn(0.5)"))
    for i in range(1, 7): # doesn't matter which one we choose as long as we choose one of them
        print("{:<10} {:<20} {:<30} {:<40}".format(str(i), str(inter1[i]), str(inter3[i]), str(inter5[i])))
    print("{:<10} {:<20} {:<30} {:<40}".format("True", math.sin(0.1), math.sin(0.3), math.sin(0.5)))
    input() # For when we are done and want to take a look at the output and are possibly not running this through the terminal

'''
This is the interpolation formula for the Divided Differences Equation, written in a method.

method: p

return type: list

parameters:
    table   [list] The XsubI values that we are going to do

    Value [float] the value that we are interpolating at.

'''
def p(table, value): 
    retVal = []
    for i in range(len(table)):
        if i == 0:
            retVal.append(float(math.sin(table[i])) + (value - table[i]))
        else:
            summation = 0
            retVal.append(retVal[i-1] * (math.sin(table[i]) - math.sin(table[i-1])) / (table[i]  - table[i-1]))

    return retVal
'''
This is a method that calculates the divided differences of the return table iteratively.

method: divideddifference

return type: list

parameters: 

table   [list] numbers that have had sin performed on them for manipulation
xsubi   [list] a list of numbers that are given in the programming assignment to be performed and calculated upon

'''
def divideddifference(table, xsubi):
    arr = []
    for i in range(len(table)):
        if i == 0:
            continue
        else:
            arr.append((table[i] - table[i-1]) / (xsubi[i] - xsubi[i-1]))
    return arr
main()