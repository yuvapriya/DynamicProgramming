def memoize(f):
    # define "wrapper" function that checks cache for
    # previously computed answer, only calling f if this
    # is a new problem.
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)  
        print memf.cache.keys() 
        print memf.cache.values()         
        return memf.cache[x]

    # initialize wrapper function's cache.  store cache as
    # attribute of function so we can look at its value.
    memf.cache = {}
    return memf
   
'''Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want),
or report that it's not possible to select coins in such a way that they sum up to S.  '''
'''http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg'''
def CoinsToSum(sum):
    Min = {}
    ValAdded = {}
    Min[0] = 0
    ValAdded[0]=0
    for i in range(1,sum+1):
        Min[i] = float("inf")
    for i in range(1,sum+1):
        for j in (1,3,5):
            if(j<=i and Min[i-j]+1<Min[i]):
                Min[i] = Min[i-j]+1
                ValAdded[i] = j
                
    # Print the values to reach this sum
    print 'Total Coins needed' , Min[sum]
    i=sum
    while(i>0):
        print ValAdded[i]
        i=i-ValAdded[i]
    return Min[sum], ValAdded[sum]
                
print CoinsToSum(11)