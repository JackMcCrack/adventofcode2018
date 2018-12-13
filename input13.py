#!/usr/bin/env python3


f=open('input13')
field=list(f)
f.closed

carts=[]
crash=0
tick=0

class Cart(object):
    def __init__(self, y, x, direction, crashed=0):
        self.y = y
        self.x = x
        if direction in ('>', '<', '^', 'v'):
            if direction == '>':
                self.direction = 'r'
            elif direction == '<':
                self.direction = 'l'
            elif direction == '^':
                self.direction = 'u'
            elif direction == 'v':
                self.direction = 'd'

        self.crossings = 0
        self.crashed = crashed

    def move(self):
        mv={}
        mv['l'] = [-1,0]
        mv['r'] = [1,0]
        mv['u'] = [0,-1]
        mv['d'] = [0,1]
        if self.crashed == 0:
            self.x += mv[self.direction][0]
            self.y += mv[self.direction][1]

    def crash(self):
        self.crashed = 1
    def turn(self):
        if field[self.y][self.x] in ('\\', '/'):
            # curve
            if field[self.y][self.x] == '\\':
                if self.direction == 'l':
                    self.direction = 'u'
                elif self.direction == 'r':
                    self.direction = 'd'
                elif self.direction == 'u':
                    self.direction = 'l'
                elif self.direction == 'd':
                    self.direction = 'r'
            elif field[self.y][self.x] == '/':
                if self.direction == 'l':
                    self.direction = 'd'
                elif self.direction == 'r':
                    self.direction = 'u'
                elif self.direction == 'u':
                    self.direction = 'r'
                elif self.direction == 'd':
                    self.direction = 'l'

        
        elif field[self.y][self.x] in ('+'):
            # crossing
            if self.crossings % 3 == 0:
                #counterclockwise
                if self.direction == 'l':
                    self.direction = 'd'
                elif self.direction == 'r':
                    self.direction = 'u'
                elif self.direction == 'u':
                    self.direction = 'l'
                elif self.direction == 'd':
                    self.direction = 'r'
            elif self.crossings % 3 == 1:
                self.direction = self.direction
            elif self.crossings % 3 == 2:
                #clockwise
                if self.direction == 'l':
                    self.direction = 'u'
                elif self.direction == 'r':
                    self.direction = 'd'
                elif self.direction == 'u':
                    self.direction = 'r'
                elif self.direction == 'd':
                    self.direction = 'l'
            self.crossings += 1

            


# setup - find carts, "fix" tracks
for y in range(len(field)):
    for x in range(len(field[y])-1):
        if field[y][x] in ('>', '<', '^', 'v'):
            carts.append(Cart(y, x, field[y][x]))

            if field[y][x] in ('>', '<'):
                field[y] = field[y].replace(field[y][x],'-', 1)
            if field[y][x] in ('^', 'v'):
                field[y] = field[y].replace(field[y][x],'|', 1)

        print(field[y][x], end="")
    print('')

while crash < 1: 
    for i in range(len(carts)):
        carts[i].move()
        for j in range(len(carts)):
            if j != i and carts[j].y == carts[i].y and carts[j].x == carts[i].x:
                crash += 1
                carts[i].crash()
                carts[j].crash()
                print('CRASH: ', carts[i].x,'x', carts[i].y, tick)
        carts[i].turn()
    tick += 1
