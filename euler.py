h = 0.25
x = [h * i for i in range(0, 15)]
y = [1]
for n in range(0, len(x)):
    if n == 0:
        continue
    else:
        function = (x[n - 1] * y[n - 1]) + 4 * x[n-1] / y[n-1]
        y.append(y[n-1] + (h * function))
print("{:<10} {:<10} {:<10}".format("h", "x", "yh(x)"))
for i in range(0, len(x)):
    xi = round(x[i], 4)
    yi = round(y[i], 4)
    print("{:<10} {:<10} {:<10}".format(h, xi, yi))