#also similar to UVA problem 100

longest=0
longeststart=0
#cycle length of 1 to 1 is 1
lengths=[1]
#initialise as -1 for not yet cycled through
for k in range(1, 1000000):
    lengths.append(-1)

#basic idea of solution:
#start with a value, e.g. 15
#chain is 15->46->23->70->35->106->53->160->80->40->20->10->5->16->8->4->2->1
#if cycle length of 46 is known, then cycle length of 15 is 1 more than that
#so we can use memorization of lengths, when a sequence reaches a known cycle
#just add that sequence cycle length
#its still slow though, but managable
    
i=1000000

while i>1:
    #work the chain out. using variable current since i is the variable to loop
    current=i
    #count no of steps in chain
    steps=0
    while current!=1:
        steps+=1
        if current%2==0:
            current=current//2
        else:
            current=3*current+1
        #check if in table
        if current<1000000:
            if lengths[current-1]>0:
                steps+=lengths[current-1]
                break
    lengths[i-1]=steps
    #if longest, then update count+stored starting no
    if lengths[i-1]>longest:
        longest=lengths[i-1]
        longeststart=i
    i-=1
print(longest, longeststart)
