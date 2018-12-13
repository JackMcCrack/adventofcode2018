#!/usr/bin/env python3 

f=open('input02')
asf=list(f)
f.closed
countaszwo = 0
countasdrei = 0

for a in asf:
    zwo = 0
    drei = 0
    for i in a:
        maxa = 0
        for j in a:
            if i == j:
                maxa+=1
        if maxa == 2:
            zwo = 1
        if maxa == 3:
            drei = 1
    countaszwo+=zwo
    countasdrei+=drei

print(countaszwo)
print(countasdrei)

print(countaszwo*countasdrei)


