blocks = int(input("Number of blocks: "))

#for base blocks
bblocks = 1
n=blocks
for i in range(blocks):
    if n > bblocks:
        n=n-bblocks
        bblocks+=1
    else:
        break
print("base blocks for the pyramid are ",bblocks)

#height
height = 0
n=blocks
while n >= bblocks:
    if n!=0:
        n = n - bblocks
        bblocks= bblocks-1
        height+=1
    else:
        break
print("height of the pyramid is ", height)
