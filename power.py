"""
Write a program to implement power of an element using DAC.
"""


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


x = int(input("Enter the number: "))
n = int(input("Enter the power "))

print(power(x, n))
