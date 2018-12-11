#!/usr/bin/env python3 

def read_node(a,x):
    child, data = a[x:x+2]
    return child, data


class Node(object):
    def __init__(self, data=[]):
        self.data = data
        self.children = []

    def set_data(self, data):
        self.data = data
    def add_child(self, obj):
        self.children.append(obj)


f=open('input08_')
asf=list(f)
f.closed



asdf=[int(a) for a in asf[0].split()]

print(read_node(asdf,0))

root=Node()

