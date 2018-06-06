import optimization as op
import time
import dorm

s = [1,4,3,2,7,3,6,3,2,4,5,3]
domain = [(0,9)]*len(s)
'''
print 'fix:',
start = time.clock()
print op.schedulecost(s)
op.printschedule(s)
print 'running time',time.clock()-start
print

print 'random optimization:',
start = time.clock()
sol = op.randomoptimize(domain)
print op.schedulecost(sol)
op.printschedule(sol)
print 'running time',time.clock()-start
print

print 'hill climb:',
start = time.clock()
sol = op.hillclimb(domain)
print op.schedulecost(sol)
op.printschedule(sol)
print 'running time',time.clock()-start
print 

print 'annealing optimization:',
start = time.clock()
sol = op.annealingoptimize(domain)
print op.schedulecost(sol)
op.printschedule(sol)
print 'running time',time.clock()-start
print

print 'genetic optimization:',
start = time.clock()
sol = op.geneticoptimize(domain)
print op.schedulecost(sol)
op.printschedule(sol)
print 'running time',time.clock()-start
print
'''
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
