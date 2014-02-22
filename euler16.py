#python's ability to handle big integers easily helps again...

number=2**1000
#just take 2^1000, then convert to string, then add individual digits
number = str(number)
total=0
for digit in number:
    total+=int(digit)
print(total)
