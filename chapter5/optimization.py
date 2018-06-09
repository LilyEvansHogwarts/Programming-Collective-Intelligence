import time
import random
import math

people = [('Seymour','BOS'),('Franny','DAL'),('Zooey','CAK'),('Walt','MIA'),('Buddy','ORD'),('Les','OMA')]

destination = 'LGA'

flights = {}
for line in file('schedule.txt'):
    origin,dest,depart,arrive,price = line.strip().split(',')
    flights.setdefault((origin, dest), [])
    flights[(origin, dest)].append((depart, arrive, int(price)))

def getminutes(t):
    x = time.strptime(t, '%H:%M')
    return x[3]*60+x[4]

def printschedule(r):
    for d in range(len(r)/2):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin, destination)][r[2*d]]
        ret = flights[(destination, origin)][r[2*d+1]]
        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,out[0],out[1],out[2],ret[0],ret[1],ret[2])

def schedulecost(sol):
    totalprice = 0
    totalwait = 0
    latestarrival = 0
    earliestdep = 24*60
    for d in range(len(sol)/2):
        origin = people[d][1]
        out = flights[(origin, destination)][sol[2*d]]
        ret = flights[(destination, origin)][sol[2*d+1]]
        totalprice += out[2] + ret[2]
        a = getminutes(out[1])
        b = getminutes(ret[0])
        latestarrival = max(a, latestarrival)
        earliestdep = min(b, earliestdep)
        totalwait += b - a
    totalwait += (latestarrival - earliestdep)*len(sol)/2
    if latestarrival>earliestdep:
        totalprice += 50
    return totalprice+totalwait

def randomoptimize(domain, costf = schedulecost):
    best = 999999999
    bestr = None
    for i in range(1000):
        r = [random.randint(k[0], k[1]) for k in domain]
        cost = costf(r)
        if cost < best:
            best = cost
            bestr = r
    return bestr

def hillclimb(domain, costf = schedulecost):
    sol = [random.randint(k[0],k[1]) for k in domain]
    best = costf(sol)

    while 1:
        flag = 0
        neighbors = []
        for i in range(len(domain)):
            if sol[i]>domain[i][0]:
                neighbors.append(sol[:i]+[sol[i]-1]+sol[i+1:])
            if sol[i]<domain[i][1]:
                neighbors.append(sol[:i]+[sol[i]+1]+sol[i+1:])

        for neigh in neighbors:
            cost = costf(neigh)
            if cost<best:
                flag = 1
                best = cost
                sol = neigh

        if flag == 0:
            break
    return sol

def annealingoptimize(domain,costf=schedulecost,T=10000.0,cool=0.95,step=1):
    vec = [random.randint(k[0],k[1]) for k in domain]
    while T>0.1:
        i = random.randint(0,len(domain)-1)
        dir = random.randint(-step,step)
        # vecb = vec is different from vecb = vec[:]
        # vecb = vec let vecb point to the same data as vec
        # vecb = vec[:] copy vec to vecb
        vecb = vec[:]
        vecb[i] = min(domain[i][1],max(domain[i][0], vecb[i]+dir))

        ea = costf(vec)
        eb = costf(vecb)

        if (eb<ea or random.random()<pow(math.e,-(eb-ea)/T)):
            vec = vecb
        T *= cool
    return vec

def geneticoptimize(domain,costf=schedulecost,popsize=50,step=1,mutprob=0.2,elite=0.2,maxiter=100):
    def mutate(vec):
        i = random.randint(0,len(domain)-1)
        if random.random()<0.5 and vec[i]>domain[i][0]:
            return vec[:i]+[vec[i]-step]+vec[i+1:]
        elif vec[i]<domain[i][1]:
            return vec[:i]+[vec[i]+step]+vec[i+1:]
        return vec

    def crossover(r1,r2):
        i = random.randint(1,len(domain)-2)
        return r1[:i]+r2[i:]

    pop = []
    for i in range(popsize):
        vec = [random.randint(k[0],k[1]) for k in domain]
        pop.append(vec)

    topelite = int(elite*popsize)

    for i in range(maxiter):
        scores = [(costf(v),v) for v in pop]
        scores.sort()
        ranked = [v for (s,v) in scores]
        pop = ranked[:topelite]
        while len(pop)<popsize:
            if random.random()<mutprob:
                c = random.randint(0,topelite)
                pop.append(mutate(ranked[c]))
            else:
                c1 = random.randint(0,topelite)
                c2 = random.randint(0,topelite)
                pop.append(crossover(ranked[c1],ranked[c2]))

    return scores[0][1]


