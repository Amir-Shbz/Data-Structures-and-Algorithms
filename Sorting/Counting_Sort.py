A = list(map(int, input().split(" ")))

mx = max(A)
B = [0] * (mx+1)

for i in A:
    B[i] += 1

for i in range(len(B)):
    for j in range(B[i]):
        print(i, end=" ")    