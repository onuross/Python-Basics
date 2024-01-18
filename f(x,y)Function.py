xMax = 3
xMin = -3
yMax = 3
yMin = -3
fTotal = 0
counter = 0
noResultCounter = 0
for x in range(xMin, xMax + 1):
    for y in range(yMin, yMax + 1):
        if x + y != 0:
            counter += 1
            function = ((2 * x) + (3 * y) - (4 * x * y) + 5) / (x + y)
            fTotal += function
        else:
            print(f"There is no result for f({x},{y})")
            noResultCounter += 1
    print(function)
    average = fTotal / counter
    print(average)
