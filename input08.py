#!/usr/bin/env python3 

f=open('input08_')
asf=list(f)
f.closed

def readnode(l=[], x=0):
    c=0
    m=0
    if x+1 < len(l):
        ### Read child
        c = int(l[x])
        ### Read meta
        m = int(l[x+1])
    return (c, m)

for a in asf:
    b = a.split()
print(b)
x = 0
d = []
todo=[]


while x < len(b):
    c,m = readnode(b,x)
    x+=2

### if child == 0 read metadata
    ### pop stack read next
    

### if cild > 0, push stack read request    
