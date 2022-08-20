l=[1,2,3,4,5,6,7]
d=2
k=l.index(d)
new_list = l[k+1:]+l[0:k+1]
print(new_list)