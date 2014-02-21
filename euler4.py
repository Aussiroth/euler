#brute force from largest
i=999
highest=0
#run all is
while i>100:
    j=999
    #run all js
    while j>100:
        #check the total
        total=i*j
        #use string to check if palindromic
        total=str(total)
        #check if palindromic
        if total==total[::-1]:
            #check if current is higher than the recorded highest
            if int(total)>highest:
                highest=int(total)
        j-=1
    i-=1
print(highest)
