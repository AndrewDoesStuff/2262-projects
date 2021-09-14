def L0(x, x0, x1, x2, x3):
    return ((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
def L1(x, x0, x1, x2, x3):
    return ((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))
def L2(x, x0, x1, x2, x3):
    return ((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))
def L3(x, x0, x1, x2, x3):
     return ((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))
def main():
    x = 5
    x0 = 1
    x1 = 2
    x2 = 3
    x3 = 4
    y0 = 2
    y1 = 4
    y2 = 9
    y3 = 16
    j0 = L0(x, x0, x1, x2, x3)
    j1 = L1(x, x0, x1, x2, x3)
    j2 = L2(x, x0, x1, x2, x3)
    j3 = L3(x, x0, x1, x2, x3)            
    value = (y0 * j0) + (y1 * j1) + (y2 * j2) + (y3 * j3)
    print(str(value))
main()