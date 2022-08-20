n=int(input())
lst=list(map(int,input().strip().split()))
A=[]
for i in range(n):
    ele=lst.count(lst[i])
    A.append(ele)
print(A)
    