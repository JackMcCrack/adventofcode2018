#!/usr/bin/env python3 

gridsn = 9995

pg=[[10] * 302 for i in  range(302)]
ps=[[10] * 302 for i in  range(302)]
high=0
low =0
maxpower=[0,0]
minpower=[0,0]

for x in range(1,301):
    for y in range(1,301):
        rid = x + 10
        p = ( rid * y + gridsn ) * rid % 1000
        if p >= 100:
            pl = int(str(p)[0])-5
        else:
            pl = -5
        pg[x][y] = pl


for x in range(1,299):
    for y in range(1,299):
        total=0
        for dx in range(0,3):
            for dy in range(0,3):
                total += pg[x+dx][y+dy]
        ps[x][y]=total
        if high < total:
            high = total
            maxpower = [x,y]
        if low > total:
            low = total
            minpower = [x,y]

print(maxpower, high)
print(minpower, low)
