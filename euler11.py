try:
    infile = open('euler11in.txt.', 'r')
except:
    print('error')
data=[]
while True:
    #keep taking in input till EOF
    raw = infile.readline()
    #if EOF then break
    if raw=="":
        break
    #else enter into data array to process
    #split via spaces to individual numbers in grid
    data.append(raw.split())
#convert numbers in data from string to integers
for i in range(0, len(data)):
    data[i]=[int(x) for x in data[i]]
#do all the checks
highest=0

#horizontal first
for i in range(0, len(data)):
    #i is the row looking at!
    #so keep on row and check through!
    for j in range(0, len(data)-4):
        #current sequence of 4
        #then just multiply the 4 in a row
        current=1
        for k in range(0, 4):
            current*=data[i][j+k]
        if current>highest:
            highest=current

#vertical test.
#similar to horizontal
for j in range(0, len(data)):
    #j is column!
    #vertical=check down the column
    #just switch i and j from horizontal test!
    for i in range(0, len(data)-4):
        #current sequence of 4
        #then just multiply the 4 in a column
        #k goes with i now, since its vertical check
        current=1
        for k in range(0, 4):
            current*=data[i+k][j]
        if current>highest:
            highest=current

#diagonal test
#start with each cell that can have a diagonal
#check rightwards and downwards first

for i in range(0, len(data)-4):
    for j in range(0, len(data)-4):
        #current sequence of 4
        #add k to both i and j to move diagonally
        current=1
        for k in range(0, 4):
            current*=data[i+k][j+k]
        if current>highest:
            highest=current 
#leftwards and downwards test
for i in range(0, len(data)-4):
    for j in range(3, len(data)):
        #current sequence of 4
        #now k is minused to j, as leftward movement = minus columns
        current=1
        for k in range(0, 4):
            current*=data[i+k][j-k]
        if current>highest:
            highest=current
            
print(highest, durr)
infile.close()
