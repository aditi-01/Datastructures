import numpy as np
n=list(map(int, input().strip().split()))
i=int(input())
a=int(input())
n.insert(i,a)
n=np.array(n)

print(n)