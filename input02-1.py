#!/usr/bin/env python3 


f=open('input02')
asf=list(f)
f.closed

last=""
for a in asf:
    for last in asf:
        count = 0
        for i in range(len(a)):
            if last[i] != a[i]:
                count+=1
        if count == 1:
            print(str(count) + " " + last + "  " + a)



