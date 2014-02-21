#iterative run to find fibonaci
first=1
second=1
total=0
#loop until fibonacci numbers reach 4mil
while first<4000000:
    #first is the larger of the 2 numbers
    first, second=first+second, first
    #modulo divide to check of even
    if first%2==0:
        total+=first
print("The total is", total)
