#Q15 is essentially a combinatorics problem
#no of ways = (n+m!)/(n!m!)
#however, a programming method is shown below

#represent grid as 2D array
#no of ways is equal to
#no of ways to point left of it+no of ways to point top of it

#IMPORTANT NOTE: 20x20 boxes = 21x21 lines of points!

grid=[]
for i in range(0, 21):
    horizontal=[]
    for j in range(0, 21):
        horizontal.append(0)
    grid.append(horizontal)
#there is exactly one way to move from a point to the same point
grid[0][0]=1

#update edges first.
#keeps things simpler.
for i in range(0, 21):
    grid[0][i]=1
for i in range(0, 21):
    grid[i][0]=1
#then keep updating values of the grid, starting from left-right, top-down
for i in range(1, 21):
    for j in range(1, 21):
        grid[i][j]=grid[i][j-1]+grid[i-1][j]
print(grid[20][20])
