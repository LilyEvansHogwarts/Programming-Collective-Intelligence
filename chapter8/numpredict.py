from random import random, randint
import math
from pylab import *

def wineprice(rating,age):
    peak_age = rating-50
    price = rating/2
    if age>peak_age:
        price = price*(5-(age-peak_age))
    else:
        price = price*5*(age+1)/peak_age
    if price<0: price = 0
    return price

def wineset1():
    rows = []
    for i in range(200):
        rating = random()*50+50
        age = random()*50
        price = wineprice(rating,age)
        price *= random()*0.4+0.8
        rows.append({'input':(rating,age),'result':price})
    return rows

def euclidean(v1,v2):
    d = [pow(v1[i]-v2[i],2) for i in range(len(v1))]
    return math.sqrt(sum(d))

def getdistance(data,vec1):
    distancelist = []
    for i in range(len(data)):
        vec2 = data[i]['input']
        distancelist.append((euclidean(vec1,vec2),i))
    distancelist.sort()
    return distancelist

def knnestimate(data,vec1,k=5):
    dlist = getdistance(data,vec1)
    avg = 0.0
    for i in range(k):
        idx = dlist[i][1]
        avg += data[idx]['result']
    return avg/k

def inverseweight(dist,num=1.0,const=0.1):
    return num/(dist+const)

def substractweight(dist,const=1.0):
    return max(0,const-dist)

def gaussian(dist,sigma=10.0):
    return math.e**(-dist**2/(2*sigma**2))

def weightedknn(data,vec1,k=5,weightf=gaussian):
    dlist = getdistance(data,vec1)
    avg = 0.0
    totalweight = 0.0
    for i in range(k):
        idx = dlist[i][1]
        weight = weightf(dlist[i][0])
        avg += weight*data[idx]['result']
        totalweight += weight
    return avg/totalweight

def dividedata(data,test=0.05):
    trainset = []
    testset = []
    for row in data:
        if random()<test:
            testset.append(row)
        else:
            trainset.append(row)
    return trainset,testset

def testalgorithm(algf,trainset,testset):
    error = 0.0
    for row in testset:
        guess = algf(trainset,row['input'])
        error += (row['result']-guess)**2
    return error/len(testset)

def crossvalidate(algf,data,trials=100,test=0.05):
    error = 0.0
    for i in range(trials):
        trainset,testset = dividedata(data,test)
        error += testalgorithm(algf,trainset,testset)
    return error/trials

def wineset2():
    rows = []
    for i in range(300):
        rating = random()*50+50
        age = random()*50
        aisle = float(randint(1,20))
        bottlesize = [375.0,750.0,1500.0,3000.0][randint(0,3)]
        price = wineprice(rating,age)
        price *= bottlesize/750
        price *= random()*0.9+0.2
        rows.append({'input':(rating,age,aisle,bottlesize),'result':price})
    return rows

def rescale(data,scale):
    scaleddata = []
    for row in data:
        scaled = [scale[i]*row['input'][i] for i in range(len(scale))]
        scaleddata.append({'input':scaled,'result':row['result']})
    return scaleddata

def createcostfunction(algf,data):
    def costf(scale):
        sdata = rescale(data,scale)
        return crossvalidate(algf,sdata,trials=10)
    return costf

weightdomain = [(0,20)]*4

def randomoptimize(domain,costf):
    best = 999999999
    bestr = None
    for i in range(1000):
        r = [randint(k[0],k[1]) for k in domain]
        cost = costf(r)
        if cost<best:
            best = cost
            bestr = r
    return bestr

def hillclimb(domain,costf):
    sol = [randint(k[0],k[1]) for k in domain]
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

def annealingoptimize(domain,costf,T=10000.0,cool=0.95,step=1):
    vec = [randint(k[0],k[1]) for k in domain]
    while T>0.1:
        i = randint(0,len(domain)-1)
        dir = randint(-step,step)
        vecb = vec[:]
        vecb[i] = min(domain[i][1],max(domain[i][0],vecb[i]+dir))
        ea = costf(vec)
        eb = costf(vecb)
        if eb<ea or random()<pow(math.e, -(eb-ea)/T):
            vec = vecb
        T *= cool
    return vec

def geneticoptimize(domain,costf,popsize=50,step=1,mutprob=0.2,elite=0.2,maxiter=20):
    def mutate(vec):
        i = randint(0,len(domain)-1)
        if random()<0.5 and vec[i]>domain[i][0]:
            return vec[:i]+[vec[i]-step]+vec[i+1:]
        elif vec[i]<domain[i][1]:
            return vec[:i]+[vec[i]+step]+vec[i+1:]
        else:
            return vec
    def crossover(r1,r2):
        i = randint(1,len(domain)-2)
        return r1[:i]+r2[i:]
    pop = []
    for i in range(popsize):
        pop.append([randint(k[0],k[1]) for k in domain])

    toplite = int(popsize*elite)

    for i in range(maxiter):
        scores = [(costf(v),v) for v in pop]
        scores.sort()
        pop = [v for (s,v) in scores[:toplite]]
        while len(pop)<popsize:
            if random()<mutprob:
                c = randint(0,toplite-1)
                pop.append(mutate(pop[c]))
            else:
                c1 = randint(0,toplite-1)
                c2 = randint(0,toplite-1)
                pop.append(crossover(pop[c1],pop[c2]))
    return scores[0][1]

def wineset3():
    rows = wineset1()
    for row in rows:
        if random()<0.5:
            row['result'] *= 0.5
    return rows

def probguess(data,vec1,low,high,k=5,weightf=gaussian):
    dlist = getdistance(data,vec1)
    nweight = 0.0
    tweight = 0.0
    for i in range(k):
        idx = dlist[i][1]
        weight = weightf(dlist[i][0])
        v = data[i]['result']
        if v<=high and v>=low:
            nweight += weight
        tweight += weight
    if tweight == 0: return 0
    return nweight/tweight

def cumulativegraph(data,vec1,high,k=5,weightf=gaussian):
    t1 = arange(0.0,high,0.1)
    cprob = array([probguess(data,vec1,0,v,k,weightf) for v in t1])
    plot(t1,cprob)
    show()

def probabilitygraph(data,vec1,high,k=5,weightf=gaussian,ss=5.0):
    t1 = arange(0,high,0.1)
    probs = [probguess(data,vec1,v,v+0.1,k,weightf) for v in t1]
    smoothed = []

    for i in range(len(probs)):
        sv = 0.0
        for j in range(0,len(probs)):
            dist = abs(i-j)*0.1
            weight = gaussian(dist,sigma=ss)
            sv += weight*probs[j]
        smoothed.append(sv)
    smoothed = array(smoothed)
    plot(t1,smoothed)
    show()

def preprocess(data):
    mean = []
    var = []
    for i in range(len(data[0]['input'])):
        mean.append(sum([d['input'][i] for d in data])*1.0/len(data))
        var.append(math.sqrt(sum([(d['input'][i]-mean[i])**2 for d in data])/len(data)))
    new_data = []
    for i in range(len(data)):
        input = [(data[i]['input'][j] - mean[j])/var[j] for j in range(len(data[i]['input']))]
        new_data.append({'input':input,'result':data[i]['result']})
    return new_data

