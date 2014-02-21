#using sieve of erastothenes
#take high n, then find all primes, then take the 10001st
n=10**6
primes = []
#make a list of primes
for i in range(2, n+1):
    primes.append(i)
i=0
while i<len(primes):
    #if number is already deleted in the sieve, move on
    if primes[i]==0:
        i+=1
    #otherwise, delete all multiples of the prime remaining in sieve
    else:
        current=primes[i]
        j=i+current
        while j<len(primes):
            primes[j]=0
            j+=current
        i+=1
#delete all the 0 placeholders for deleted value
primes = [x for x in primes if x!=0]
print(primes[10000])
