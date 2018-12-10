#!/usr/bin/env python3 

f=open('input05')
asf=list(f)
f.closed


for s in asf:
    for l in range(65,91):
        a = s
        #print(a)
        repeat = 1
        while repeat > 0:
            repeat = 0
            for x in range(len(a),0,-1):
                if x < len(a):
                    if a[x] == chr(l) or a[x] == chr(l+32):
                        a = a[0:x] + a[x+1:len(a)]
        print('>', chr(l), chr(l+32))


        #### PART1:
        repeat = 1
        while repeat > 0:
            repeat = 0
            for x in range(len(a)):
                if x < len(a)-1:
                    d = ord(a[x]) - ord(a[x+1])
                    if d == 32 or d == -32:
                        #print(a[0:len(a)-1])
                        repeat = 1
                        if x > 0 and x+2 < len(a):
                            a = a[0:x] + a[x+2:len(a)]
                        else:
                            if x == 0:
                                a = a[x+2:len(a)]
                            else:
                                a = a[0:x-1]
                        #print(a)
        print(len(a)-1)
