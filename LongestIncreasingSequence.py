'''http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg'''
def LongestIncreasingSequence(Arr):
    Sol={}
    Sol[0] = 1
    max_so_far = 1 # Use this for arr ending with val that is not part of LIS(eg:5,3,4,2) Sol for 2 should not remain 1
    for i in range(1,len(Arr)):
        Sol[i] = 1
        for j in range(0,i):
            if(Arr[j]<Arr[i] and Sol[j]+1>Sol[i]):
                Sol[i] = Sol[j] + 1
                print 'LIS so far till', Arr[i], 'is', Sol[i] 
                if(max_so_far<Sol[i]):
                    max_so_far = Sol[i]
        if(Sol[i]<max_so_far):
            Sol[i] = max_so_far         
    lastIndex = len(Arr) - 1
    return Sol[lastIndex]
    
print LongestIncreasingSequence([5,3,4,8,6,7,9])