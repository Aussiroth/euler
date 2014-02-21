#smallest number - multply by all unique factors

#find prime factors
def findfactors(number):
    #count the largest factor
    factors=[]
    #run until number is divided down to 1
    i=2
    while number>1:
        if number%i==0:
            factors.append(i)
            number=number//i
        else:
            #if not modular divide, move on to next number to check if factor
            i+=1
    return factors

i=20
smallest=1
unique=[]
while i>1:
    #find all prime factors of the number
    factors = findfactors(i)
    #add the prime numbers if they aren't inside unique factors
    j=0
    k=0
    newunique=[]
    #concatanate the 2, if the factors are the same only add one, not both from each
    while k<len(unique) and j<len(factors):
        #if the same, add one, then move on
        if unique[k]==factors[j]:
            newunique.append(unique[k])
            j+=1
            k+=1
        #else if factor in unique is larger, then catch up factors first
        elif unique[k]>factors[j]:
            newunique.append(factors[j])
            j+=1
        #if factor in unique is smaller, then catch up unique first
        else:
            newunique.append(unique[k])
            k+=1
    #contanate all those that didnt compare
    newunique+=unique[k:]
    newunique+=factors[j:]
    unique=sorted(newunique)
    i-=1
for factor in unique:
    smallest*=factor
print(smallest)
