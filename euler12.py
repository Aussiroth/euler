def countfactor(number):
    factors=0
    #divide through until square root of number to find factors,
    #then x2.
    for i in range(1, int(number**0.5)):
        if number%i==0:
            factors+=1
    factors*=2
    #remove if there is double counted factor if square root of number is a factor
    #e.g. 6*6=36, but 6 should only be counted once, so remove the double count
    if number%(number**0.5)==0:
        factors-=1
    return factors

#while loop since end point is unknown
triangle=1
factors = countfactor(triangle)
i=2
while factors<500:
    #count up triangle numbers
    triangle+=i
    #use function to get no of factors
    factors = countfactor(triangle)
    i+=1
print(triangle)
