A = list(map(int, input().split(" ")))

for i in range(1, len(A)):
    j = i
    item = A[i]
    while A[j-1]>item and j > 0:
        A[j] = A[j-1]
        j -= 1
    A[j] = item    
    
print(A)    