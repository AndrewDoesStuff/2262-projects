import numpy as np
def main():
    a = np.array([[2,1,-1,-2],[4,4,1,3],[-6,-1,10,10],[2,1,8,4]])
    b = np.array([2,4,-5,1])
    x = np.linalg.solve(a, b)
    a = np.round(a, 3)
    print("Ax = b")
    print("A = ")
    for i in a:
        for j in i:
            print(j, end=" ")
        print("\n")
    print("x =")
    for i in x:
        # print(i, end="\n")
        print("{:<}".format(i))
    print("\nB=")
    for i in b:
        print(i, end="\n")
main()