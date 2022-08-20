from math import floor


n=int(input())
lst = list(map(int,input().strip().split()))
A=sorted(lst)
def median(lst,n,A):
    if n==0:
        return -1
    elif n==1:
        return(A[0])
    elif len(lst)%2!=0:
        i=n//2
        return (A[i])
    elif len(lst)%2==0:
        i=n//2
        med=floor((A[i]+A[i+1])/2)
        return(med)

def mean(lst,n):
    sum=0
    for i in range(n):
        sum=lst[i]+sum
    mea = sum/n
    return(mea)

ans1=median(lst,n,A)
ans2=mean(lst,n)

print(ans1)
print(ans2)