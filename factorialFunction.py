
def factorial(number = int(input("Enter The Number:"))):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
print(factorial())


# 2.way
#
# number= int(input("Enter The Number:"))
# result = 1
# for x in range(number,0,-1):
#     result *= x
#
# print(f"Factorial Of {number} ---> {number}! = {result}")