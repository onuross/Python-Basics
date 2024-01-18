# 1 1 2 3 5 8 13 21 34 55
num1 = 1
num2 = 1
fibonacciMax = 0
print(num1)
while fibonacciMax < 1000:
    print(num2)
    fibonacciMax = num1 + num2
    num1 = num2
    num2 = fibonacciMax

# 2.way recursion

def fibonacci(number=int(input("Enter The Number:"))):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci())


