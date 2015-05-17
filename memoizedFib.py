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
    
def Fibonacci(x):
    if x==0 or x == 1:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci (x-2)
        
Fibonacci = memoize(Fibonacci)

print Fibonacci(10)