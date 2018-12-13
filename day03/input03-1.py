#!/usr/bin/env python3 

f=open('input03')
asf=list(f)
f.closed
msize = 1000
matrix=[]

for y in range(msize):
    matrix.append([0]*msize)

for a in asf:
    b=a.split()
    pos = b[2].split(',')
    size= b[3].split('x')
    
#    print(pos[0] + " " + pos[1])
#    print(size[0] + " " + size[1])
    
    for y in range(int(size[0])):
        for x in range(int(size[1])):
            matrix[y + int(pos[0])][x + int(pos[1])] += 1

count = 0
for y in range(msize):
    for x in range(msize):
        if matrix[x][y] > 1:
            count += 1            
print(count)
for a in asf:
    fit = 1
    b=a.split()
    pos = b[2].split(',')
    size= b[3].split('x')
    
#    print(pos[0] + " " + pos[1])
#    print(size[0] + " " + size[1])
    
    for y in range(int(size[0])):
        for x in range(int(size[1])):
            if matrix[y + int(pos[0])][x + int(pos[1])] != 1:
                fit = 0
    if fit == 1:
        print(b[0])
