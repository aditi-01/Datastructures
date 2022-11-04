num = 1234

def extract(num):
    x=[]
    while num>0:
        a=num%10
        num=num//10
        x.append(a)
    x.reverse()
    return x
def pow(x,y):
    return x**y

def isarm(num):
    x=extract(num)
    print(x)
    sum1=0
    for i in x:
        sum1=sum1+pow(i,len(x))
    if sum1==num:
        return True
    else:
        return False

print(isarm(1253))