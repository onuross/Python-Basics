# 1.way
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))

print(gcd(num1, num2))

# 2.way
num1 = int(input("Enter The First Number:"))
num2 = int(input("Enter The Second Number:"))
gcf = 0
if num1 > num2:
    num1, num2 = num2, num1

for x in range(num1, 0, -1):
    if num1 % x == 0 and num2 % x == 0:
        gcf = x
        break

print(gcf)

