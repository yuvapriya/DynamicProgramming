def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x]=f(*x)
        return memf.cache[x]  
    memf.cache={}
    return memf

def countPaths(m,n):
    print 'Looking for',m,n
    if m==1 or n==1:
        return 1
    return countPaths(m-1,n)+countPaths(m,n-1)+countPaths(m-1,n-1)
    
countPaths = memoize(countPaths)
print countPaths(3,3)

def countPathsUsingArray(m,n):
    count = [[0 for x in range(m)] for x in range(n)]
    for x in range(m):
        count[x][0] = 1
    for x in range(n):
        count[0][x]=1
    for i in range(1,m):
        for j in range(1,n):
            count[i][j] = count[i-1][j] + count[i][j-1] + count [i-1][j-1]
    print count
    return count[m-1][n-1]
    
print countPathsUsingArray(3,3)
