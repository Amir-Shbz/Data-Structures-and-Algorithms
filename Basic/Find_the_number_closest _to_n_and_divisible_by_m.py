# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. 
# If there is more than one such number, then output the one having maximum absolute value.


def closest_number(n, m):

    return n - (n%m)


print(closest_number(13,4))