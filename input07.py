#!/usr/bin/env python3 

f=open('input07_')
asf=list(f)
f.closed
minval=ord('A')
maxval=ord('F')+1
d=[]
s=[]
for a in asf:
    s.append([a[5], a[36]])

for i in range(minval,maxval):
    t = []
    for j in range(len(s)):
        #print(chr(i), s[j])
        if chr(i) == s[j][0]:
            t.append(s[j][1])
    d.append([chr(i), t])

start=0
for i in range(len(d)):
    if len(d[i][1]) == 0:
       start=d[i][0]     
#       print(d[i][0])
    #print(d[i][0], d[i][1], len(d[i][1]))
print(start,d)



result=""


step=[]

for x in range(minval,maxval):
    #print(x, step)
    for search in chr(x):
        t=[]
        for i in range(len(d)):
            if search in d[i][1]:
                t.append(d[i][0])
            #print(search, t)
        if len(t) > 0:
            step.append([search,t])
        else:
            step.append([search,''])

print(step)


#print(step, result[len(result)-1:len(result)])
do=[]

for x in range(minval,maxval):
    for i in range(len(step)):
        if step[i][0] == chr(x):
            do.append([chr(x),sorted(set().union(step[i][1]))])

avail=[]
for x in do:
    if x[1]==[]:
        avail.append(x[0])
        print(x[0])
            

print('---', d, '\n---', do, '\n---', step, '\n---', avail)
while len(result) < (maxval-minval):
    x = avail[0]
    print(do[0], d[0])
    for y in d:
        if y[0] == x:
            for z in y[1]:
                for f in do:
                    if f == y:
                        print(f,y)
                result += x
                avail = sorted(list(set().union(avail, y[1])))
                if x in avail:
                    avail.remove(x)
        print(x, y[0], y[1], result, avail)








print(result)

















#search=start
#count=0
#step=[]
#step.append([str(0), [start],count])
##print(d)
#for x in step:
#    count+=1
#    for search in x[1]:
#        t=[]
#        for i in range(len(d)):
#            if search in d[i][1]:
#                t.append(d[i][0])
##        print(search, t)
#        if len(t) > 0:
#            step.append([search,t,count])
#        else:
#            step.append([search,'',count])
##        print(count)
#print(step)
#word=""
#
#tmp=""
#for x in range(len(step),0,-1):
#    for i in step:
#        if x == i[2]:
#            for j in i[0]:
#                #print(j, x, i)
#                if j not in tmp:
#                    tmp = tmp + j
#print(tmp)
