#!/usr/bin/env python3 

gridsn = 9995

pg=[[10] * 302 for i in  range(302)]
ps=[[[10] * 302 for i in  range(302)] for j in range(301)]

score = []
for x in range(1,301):
    for y in range(1,301):
        rid = x + 10
        p = ( rid * y + gridsn ) * rid % 1000
        if p >= 100:
            pl = int(str(p)[0])-5
        else:
            pl = -5
        pg[x][y] = pl

for s in range(1,301):
    high=0
    low =0
    maxpower=[0,0]
    minpower=[0,0]
    for x in range(1,301-s):
        for y in range(1,301-s):
            total=0
            for dx in range(0,s):
                for dy in range(0,s):
                    total += pg[x+dx][y+dy]
            ps[x][y]=total
            if high < total:
                high = total
                maxpower = [x,y]
            if low > total:
                low = total
                minpower = [x,y]

    
    score.append([maxpower, s, high])
    #print(s, minpower, low)

winner = 0
index = 0
for s in range(len(score)):
    if score[s] > winner:
        winner = score[s]
        index = s

print(winner)
