n=int(input())
for _ in range(n):
    arrsize=int(input())
    arr=list(map(int,input().strip().split()))

    arrset=set(arr)
    arrrev = sorted(arr)
    larr =[]
    for j in range(1,arrsize+1):
        ele=j
        larr.append(j)
    larr=sorted(larr)
    if (len(arr))==(len(arrset)):
        if sorted(arr)==sorted(larr):
            if arr==arrrev:
                print("Bad")
            else:
                print("Good")
        else:
            print("Bad")
    else:
        print("Bad")



        