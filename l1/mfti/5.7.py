A=[0, 1, 2, 3, 4]
tep=A[0]
for k in range(N-1):
    A[k]=A[k+1]
A[N-1]=tmp
print(A)