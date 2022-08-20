import numpy as np
n=list(map(int, input().strip().split()))
a=int(input())
n.append(a)
n=np.array(n)

print(n)
