sumofsquares=0
squareofsums=0
for i in range(1, 101):
    #add square to the sum of squares
    sumofsquares+=(i*i)
    #add number to square of sums to square later
    squareofsums+=i
#square the square of sums
squareofsums=squareofsums**2
#take difference
print(squareofsums-sumofsquares)
