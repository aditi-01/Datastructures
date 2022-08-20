def minAdjDiff(arr, n):
        ans=[]
        for i in range(n-1):
            dif= abs(arr[i]-arr[i+1])
            ans.append(dif)
        l=abs(arr[-1]-arr[0])
        ans.append(l)
        return(min(ans))

print(minAdjDiff())