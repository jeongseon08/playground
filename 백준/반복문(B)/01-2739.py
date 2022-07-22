A=int(input())
i=1
while i<10:
    print("%d * %d = %d"%(A,i,A*i))
    i=i+1 
#혹은 
for i in range(1,10):
    print(A, "*", i, "=", A*i)
