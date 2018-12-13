#!/usr/bin/env python3 

f=open('input12_sorted')
asf = list(f)
f.closed

state = asf[0]
rules = []
for r in range(1,len(asf)):
    rules.append([asf[r][0:5], asf[r][9]])
off=0
state=".." + state[0:len(state)-1]
for step in range(121):
    nextstate=""
    tmp = ".."+state+".."
    for x in range(len(state)):
        c = (tmp[x:x+5])
        for r in rules:
            if c == r[0]:
                nextstate = nextstate + r[1]
                break
        else:
            print(c, len(c))
            nextstate = nextstate + 'x'
    #state=nextstate[1:len(nextstate)]+'.'
    state=nextstate=nextstate+'.'
    off+=1




    res= tmp[4:len(tmp)]
    total=0
    for i in range(len(res)):
        if res[i] == '#':
            total += i

    print(tmp, len(tmp), off, step, total)
    if step==20:
        print(total)


res= tmp[4:len(tmp)]
total=0
for i in range(len(res)):
    if res[i] == '#':
        total += i+50000000000-120


print(total)
