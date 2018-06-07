import optimization as op
import dorm
import time

print 'fix:',
start = time.clock()
s = [0]*len(dorm.prefs)
print dorm.dormcost(s)
dorm.printsolution(s)
print 'running time',time.clock()-start
print

print 'random optimization:',
start = time.clock()
s = op.randomoptimize(dorm.domain,costf=dorm.dormcost)
print dorm.dormcost(s)
dorm.printsolution(s)
print 'running time',time.clock()-start
print

print 'hill climb:',
start = time.clock()
s = op.hillclimb(dorm.domain,costf=dorm.dormcost)
print dorm.dormcost(s)
dorm.printsolution(s)
print 'running time',time.clock()-start
print

print 'annealing optimization:',
start = time.clock()
s = op.annealingoptimize(dorm.domain,costf=dorm.dormcost)
print dorm.dormcost(s)
dorm.printsolution(s)
print 'running time',time.clock()-start
print

print 'genetic optimization:',
start = time.clock()
s = op.geneticoptimize(dorm.domain,costf=dorm.dormcost)
print dorm.dormcost(s)
dorm.printsolution(s)
print 'running time',time.clock()-start
print


