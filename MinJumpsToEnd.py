def MinJumpsToReachEnd(Arr):
    jumps={}
    jumps[0] = 0
    for i in range(1,len(Arr)):
        jumps[i] = float('inf')
        for j in range(0,i):
            #If i reachable from j i.e value @ j which is Arr[j]+j>=i
            if(j+Arr[j] >= i and jumps[j] +1 < jumps[i]):
                jumps[i] = jumps[j]+1                
    lastIndex = len(Arr) - 1
    print jumps
    return jumps[lastIndex]
    
print MinJumpsToReachEnd([1, 3, 6, 1, 0, 9])
print MinJumpsToReachEnd([1, 0, 0, 0, 8])