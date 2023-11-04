A = list(map(int, input().split(" ")))

n = len(A)
for i in range(n-1):
    for j in range(n-1,i,-1):
        if A[j] < A[j-1]:
            k = A[j]
            A[j] = A[j-1]
            A[j-1] = k
    
print(A)            