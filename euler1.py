total=0
#loop through all numbers in search range
for i in range(1, 1000):
    if i%3==0 or i%5==0:
        #check if multiple via modular divide
        total+=i
print("Total is", total)
