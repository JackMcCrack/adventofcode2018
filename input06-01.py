#!/usr/bin/env python3 

import operator

def csub(a,b):
    r=[]
    for i in range(len(a)):
        r.append(a[i]-b[i])
    return r

def cdelta(a,b):
    t = csub(a,b)
    r = abs(t[0]) + abs(t[1])
    return r

f=open('input06')
asf=list(f)
f.closed

fmax=[0]*2
fmin=[100]*2
coord=[]
for a in asf:
    a=a[0:len(a)-1].replace(" ", "")
    c = a.split(',')
    coord.append(c)
    for i in range(len(c)):
        d=int(c[i])
        coord[len(coord)-1][i]=d
        if d > fmax[i]:
            fmax[i] = d
        if d < fmin[i]:
            fmin[i] = d

#print(fmin, fmax)
#print(coord)
for i in range(len(coord)):
    coord[i] = csub(coord[i], fmin)
fmax = csub(fmax,fmin)
fmin=[0,0]
fmax[0]+=1
fmax[1]+=1

print(fmin, fmax)
deltamax=cdelta(fmax,fmin)
#[[0] * m for i in range(n)]

r=[0]*len(coord)
fa=[[['.']*len(coord) for i in range(fmax[1])] for j in range(fmax[0])]
fr=[['x']*(fmax[1]) for i in range(fmax[0])]
#print(fa)
#print(fmin, fmax)
#print(coord)
for x in range(fmax[0]):
    for y in range(fmax[1]):
        for j in range(len(coord)):
            #print(x,y,j)
            fa[x][y][j] = cdelta([x,y],coord[j])
        lmin=min(fa[x][y])
        count=0
        #print(x, y, fa[x][y])
        for j in range(len(coord)):
            if fa[x][y][j] == lmin:
                count+=1
        if count==1:
            fr[x][y] = fa[x][y].index(lmin)           




for y in range(len(fr[0])):
    for x in range(len(fr)):
        #if [x,y] in coord:
        #    fr[x][y] = 'Z'
        print(fr[x][y], end =" ")
    print("")


ign=[]
cnt=[0]*len(coord)
for j in range(len(coord)):
    count = 0
    for x in range(fmax[0]):
        for y in range(fmax[1]):
            if j == fr[x][y]:
                count+=1
                if x == 0 or y == 0 or x == len(fr[0]) or y == len(fr):
                    if j not in ign:
                        ign.append(j)
                    #print(j, 'x: ', x, 'y: ', y )
    cnt[j]=count

print(ign, cnt)
for i in range(len(coord)):
    if i not in ign:
        print(i, cnt[i])


