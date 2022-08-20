def largestAndSecondLargest(sizeOfArray, arr):
        if len(arr)==1:
            ans=[arr[0],-1]
            return(ans)
        elif len(set(arr))==1:
            ans=[arr[0],-1]
            return(ans)
        else:
            sorted_list=sorted(list(set(arr)))
            ans=[sorted_list[-1],sorted_list[-2]]
            return(ans)

print(largestAndSecondLargest(6,[1000,1000,1000,1000,1000,100]))