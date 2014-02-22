#python's ability to do large number stuff ftw
fac100=1
for i in range(2, 101):
    fac100*=i
#get total digits
totaldigits=0
fac100 = str(fac100)
for digit in fac100:
    totaldigits+=int(digit)
print(totaldigits)
