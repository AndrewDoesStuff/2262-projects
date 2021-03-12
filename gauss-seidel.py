def GaussSeidel(x, a, b):
    for i in range(0, len(a)):
        temp = b[i]
        for j in range(0, len(a)):
            if i != j:
                temp -= a[i][j] * x[j]
        x[i] = temp / a[i][i]
    return x
x = [0, 0, 0]                         
a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]] 
b = [4,7,3] 
print(x)
for i in range(0, 25):             
    x = GaussSeidel(x, a, b) 
    #print each time the updated solution 
    print(x)    