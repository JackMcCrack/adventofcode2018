#!/usr/bin/env python3 

f=open('input01')
asf=list(f)
f.closed
sss = []
for i in asf:
    sss.append(int(i))
aaa = 0
bbb= []
repeat = 1
while repeat:
    for i in sss:
        bbb.append(aaa)
        aaa = aaa + i
        for j in bbb:
            if j == aaa:
                print(aaa)
                repeat = 0

