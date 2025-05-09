# Given an Integer n, find the reverse of its digits.

def func(n):

    num = 0
    dig = 0
    m = n
    while m > 10:
        dig += 1
        m = int(m/10)

    while n > 0:
        num += (10**dig)*(n%10)
        n = int(n/10)
        dig -= 1

    return num

print(func(122))
print(func(200))
print(func(12345))