import optimization as op
import socialnetwork as so
import time

print 'random optimization:',
start = time.clock()
sol = op.randomoptimize(so.domain,so.crosscount)
print so.crosscount(sol)
print 'running time',time.clock()-start
print
so.drawnetwork(sol)


print 'hill climb:',
start = time.clock()
sol = op.hillclimb(so.domain,so.crosscount)
print so.crosscount(sol)
print 'running time',time.clock()-start
print
so.drawnetwork(sol)

print 'annealing optimization:',
start = time.clock()
sol = op.annealingoptimize(so.domain,so.crosscount)
print so.crosscount(sol)
print 'running time',time.clock()-start
print
so.drawnetwork(sol)

print 'genetic optimization:',
start = time.clock()
sol = op.geneticoptimize(so.domain,so.crosscount)
print so.crosscount(sol)
print 'running time',time.clock()-start
print
so.drawnetwork(sol)





