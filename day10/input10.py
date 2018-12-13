#!/usr/bin/env python3 

from numpy import array

f=open('input10')
asf=list(f)
f.closed

dot=[]
step=0
posmin=[0,0]
posmax=[0,0]

#print(' X', ' Y', 'vx', 'vy')
for a in asf:
    x, y, vx, vy = (int(a[10:16]), int(a[18:24]), int(a[36:38]), int(a[40:42]))
    #x, y, vx, vy = (int(a[10:12]), int(a[14:16]), int(a[28:30]), int(a[32:34]))
    dot.append([x, y, vx, vy])
    if x < posmin[0]:
        posmin[0] = x
    if x > posmax[0]:
        posmax[0] = x
    if y < posmin[1]:
        posmin[1] = y
    if y > posmax[1]:
        posmax[1] = y




run = 100
while run > 0:
    lastmin=posmin
    lastmax=posmax
    posmin=[0,0]
    posmax=[0,0]
    for i in range(len(dot)):
        dot[i][0] += dot[i][2] 
        dot[i][1] += dot[i][3] 
        x, y, vx, vy = dot[i]
        if x < posmin[0]:
            posmin[0] = x
        if x > posmax[0]:
            posmax[0] = x
        if y < posmin[1]:
            posmin[1] = y
        if y > posmax[1]:
            posmax[1] = y
    if  (lastmin[0] < posmin[0] and lastmax[0] > posmax[0]) or (lastmin[1] < posmin[1] and lastmax[1] > posmax[1]):
        print(step, posmin, posmax)
    else:
        f = open('output10-'+str(step), 'w')
        for x in range(posmin[0], posmax[0]+1):
            out=''
            for y in range(posmin[1], posmax[1]+1):
                o = '.'
                for d in dot:
                    if x == d[0] and y == d[1]:
                        o = '#'
                out=out+o
            f.write(out+'\n')
        f.close
        
        run -= 1
    step += 1 





step+=1
