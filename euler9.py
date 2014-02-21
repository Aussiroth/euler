#brute force for possible a/b/c
found=False
wanta=0
wantb=0
wantc=0
for a in range(3, 500):
    if found:
        break
    for b in range(3, 500):
        #find c via a and b
        c = (a**2+b**2)**0.5
        #check if c is an integer
        #if c is not, then mod 1 will not equal 0
        if c%1==0:
            c=int(c)
            #if a b and c total 1000, then it is found
            if a+b+c==1000:
                wanta=a
                wantb=b
                wantc=c
                found=True
                break
print(a*b*c)
