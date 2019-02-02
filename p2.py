a=map(int,raw_input().strip().split())

b=map(int,raw_input().strip().split())

def merge_arrays(a,b):
    n=len(a)+len(b)
    len_a=len(a)
    len_b=len(b)
    ar=[0 for i in range(n)]
    for i in range(n):
        if len_a > 0 and i%2==0:
            ar[i]=a[len(a)-len_a]   
            len_a-=1
        else:
            ar[i]=b[len(b)-len_b]
            len_b-=1
    return ar
            
sol=[]
ar=merge_arrays(a,b)
n=len(ar)
for i in range(n-1):
    temp=[ar[i]]
    for j in range(i,n-1):
        if ar[j]<ar[j+1]:
            temp.append(ar[j+1])
    sol.append(temp)

print sol
