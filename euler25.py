#again, python's ability to do biginteger operations extremely quickly
#makes this task a lot simpler
#in another programming language
#you can truncate excess digits off and store how many were cut off in memory when
#numbers become large

first=1
second=1
count=2
digits=0
while True:
    count+=1
    #first becomes the newer larger fibonacci number
    #then second becomes the original first fibonacci number
    first, second=first+second, first
    #this is the code for truncation
    #if first>10**10:
    #    first=first//10
    #    second=second//10
    #    digits+=1
    #if digits+len(str(first))>=1000:
    #    break
    if len(str(first))>=1000:
        break
print(count)
