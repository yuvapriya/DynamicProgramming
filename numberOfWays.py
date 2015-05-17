#Memeorize the function args and results to retrive it from cache
def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]            
    memf.cache = {}
    return memf
    

def numberOfWays(increments, totalScore, index):
    if (totalScore == 0): # Handle input 0
        return 1
    if totalScore <0 or index<0:
        return 0  
    includingLast = numberOfWays(increments, (totalScore - increments[index]), index)
    excludingLast = numberOfWays(increments, totalScore, index-1)
    return includingLast + excludingLast
 
#numberOfWays = memoize(numberOfWays)

increments = [2,3,7]
totalScore = 5
print numberOfWays(increments, totalScore, len(increments)-1)


# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/profile
# 
# Enjoy your interview!
# 
# 
# Input: increments, totalScore
# Output: Number of ways to reach totalScore
# 
# Ex 1:
# Input: [2,3,7], 5
# Output: 2
# (2+3, 3+2)