import math as m
'''
This program calculates the actual values of the Cubic Spline numerical method on certain given values.

CSC 2262 Programming Project 1

@author Andrew Hannie
@since 10/5/2020
'''


def main():
    j = [i for i in range(0, 7)] # change to 0, 8 for textbook values, and 0, 7 for given values
    xj = [17, 20, 23, 24, 25, 27, 27.7] # given values
    fxj = [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1] # given values
    # xj = [1, 2, 5, 6, 7, 8, 10, 13, 17] # textbook values
    # fxj = [3.0, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5] # textbook values
    WriteOutput(j, xj, fxj)
'''
This program writes out the values that are asked in the program.

method: WriteOutput

return type: void

parameters:
j   [list]    the given values for the j column of the calculations
xj  [list]    the given values for the xj column of the calculations
fxj [list]    the given values for fxj column of the calculations

@author Andrew Hannie
@since 10/5/2020
'''
def WriteOutput(j, xj, fxj):
    dashes = WriteDashes()
    bcdArray = list(Splines(xj, fxj))
    # b = [0 for i in range(0, len(bcdArray))]
    # c = list(b)
    # d = list(b)
    print(dashes)
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("j", "xj", "aj=f(xj)", "bj", "cj", "dj"))
    print(dashes)
    for i in range(0, len(j)): # i pick len(j) because in every case of this algorithm j xj and fxj are of the same size so i just picked one
        if i > len(bcdArray):
            print("{:<20} {:<20} {:<20} ".format(j[i], xj[i], fxj[i]))
        else:
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(j[i], xj[i], fxj[i], bcdArray[i][0], bcdArray[i][1], bcdArray[i][2]))

    print(dashes)
'''
Performs the cubic splines operations on the given data.

method: Splines

parameters:
x   [list]  the x coordinates given in the problem
y   [list]  the y coordinates given in the problem, also known as aj=f(x)
'''
def Splines(x, y):
    table = list(zip(x, y)) # puts the x and y values into a 2d list
    n = len(table) - 1 # considering n is the length of the table, and x and y are always running in parallel, n = len(table)
    h = [0 for i in range(0, n + 1)]
    alpha = list(h)
    l = list(h)
    u = list(h)
    z = list(h)
    b = list(h)
    c = list(h)
    d = list(h)
    l[0] = 1
    u[0] = 0
    z[0] = 0
    for i in range(0, n):
        h[i] = table[i+1][0] - table[i][0]
    for i in range(1, n):
        alpha[i] = (3 * ( (table[i+1][1] * h[i-1]) - (table[i][1] * (table[i+1][0] - table[i-1][0]) ) + (table[i-1][1] * h[i]) )) / (h[i-1] * h[i])
    for i in range(1, n):
        l[i] =  (2 * (table[i+1][0] - table[i-1][0])) - (h[i-1] * u[i-1])
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - (h[i-1] * z[i-1])) / (l[i])
    l[n] = 1
    u[n] = 0
    z[n] = 0
    for i in range(n - 1, -1, -1):  
        c[i] = z[i] - (u[i] * c[i+1])
        b[i] = (table[i+1][1] - table[i][1]) / (h[i] - ( h[i] * ((c[i+1] + (2 * c[i])) / 3)))
        d[i] = (c[i+1] - c[i]) / (3 * h[i])
    retList = list(zip(b, c, d))
    return retList
'''
Simple output that writes a whole bunch of dashes to make the formatting
of the table look better.

method: WriteDashes

return type: string

@author Andrew Hannie
@since 10/5/2020
'''
def WriteDashes():
    retString = ""
    for i in range(0, 110):
        retString += "-"
    return retString
main()