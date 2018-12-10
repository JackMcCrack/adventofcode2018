#!/usr/bin/env python3 


f=open('input04')
asf=list(f)
f.closed

gm = {}
gid = 0
s=0
last=None
for a in asf:
    if a[19:24] == 'Guard':
        g = a.split(' ')[3]
        gid = int(g[1:len(g)])
    if a[19:24] == 'falls':
        s=int(a[15:17])
        if gid not in gm:
            gm[gid] =[0]*60
    if a[19:24] == 'wakes':
        t=int(a[15:17])
        d=t-s
        for i in range(s,t):
            gm[gid][i] = gm[gid][i] + 1
#        if gid in gm:
#            new=gm[gid]+d
#            gm[gid]=new
   

#for g in gm:
#    print(str(g) +" "+ str(gm.get(g)) +" "+str(g*gm.get(g)))

for gid in gm:
    print(gid)
    print(gm[gid])
