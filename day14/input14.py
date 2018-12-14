#!/usr/bin/env python3


f=open('input14')
asf=list(f)
f.closed

recipe=[]
for i in range(len(asf[0])-1):
    recipe.append(int(asf[0][i]))

new = 0-len(recipe)

x = 0
y = x+1
for step in range(30121):

    total = recipe[x] + recipe[y]
    if total < 10:
        recipe.append(total)
        new += 1
    else:
        recipe.append(1)
        recipe.append(total%10)
        new += 2
        
    x = ( x + recipe[x] + 1 ) % len(recipe)
    y = ( y + recipe[y] + 1 ) % len(recipe)
print(recipe[len(recipe)-10:len(recipe)])
