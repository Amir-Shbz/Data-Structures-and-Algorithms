# Given a number n, find the sum of its digits.

def sumOfDigits(n):

    x = 0
    while n > 0:
        x += n%10
        n = int(n/10)

    return x  


print(sumOfDigits(687))