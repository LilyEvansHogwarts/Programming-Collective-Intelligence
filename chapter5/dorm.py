import random
import math

dorms = ['Zeus','Athena','Hercules','Bacchus','Pluto']

prefs = [('Toby',('Bacchus','Hercules')),
        ('Steve',('Zeus','Pluto')),
        ('Andrea',('Anthena','Zeus')),
        ('Sarah',('Zeus','Pluto')),
        ('Dave',('Athena','Bacchus')),
        ('Jeff',('Hercules','Pluto')),
        ('Fred',('Pluto','Athena')),
        ('Suzie',('Bacchus','Hercules')),
        ('Laura',('Bacchus','Hercules')),
        ('Neil',('Hercules','Athena'))]

domain = [(0,len(dorms)*2-1-i) for i in range(len(dorms)*2)]

def printsolution(vec):
    slots = []
    for i in range(len(dorms)): slots += [i,i]
    for i in range(len(vec)):
        x = vec[i]
        print prefs[i][0],dorms[slots[x]]
        del slots[x]

def dormcost(vec):
    slots = []
    cost = 0
    for i in range(len(dorms)): slots+=[i,i]
    for i in range(len(vec)):
        x = vec[i]
        dorm = dorms[slots[x]]
        pref = prefs[i][1]
        if pref[0] == dorm: cost+=0
        elif pref[1] == dorm: cost+=1
        else: cost+=3
        del slots[x]
    return cost
