number = 600851475143
#endpoint is square root of number
endpoint = int(number**0.5)
#count the largest factor
largest=0
for i in range(2, endpoint):
    if number%i==0:
        number=number/i
        largest=i
print("The highest prime factor is", largest)
