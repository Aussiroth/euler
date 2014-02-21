#note: Python can easily run BigInt operations quickly
#so no mathematical work/heuristical work needed
infile = open('euler13in.txt', 'r')
total=0
while True:
    raw = infile.readline()
    if raw=="":
        break
    else:
        number = int(raw)
        total+=number
print(total)
