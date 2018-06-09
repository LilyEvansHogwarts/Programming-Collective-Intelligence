import numpredict as num

'''
data = num.wineset3()
print num.wineprice(99.0,22.0)
print num.weightedknn(data,(99.0,22.0))
print
print (0,40),num.probguess(data,(99.0,20.0),0,40)
print (40,80),num.probguess(data,(99.0,20.0),40,80)
print (80,120),num.probguess(data,(99.0,20.0),80,120)
print (120,1000),num.probguess(data,(99.0,20.0),120,1000)
print (30,120),num.probguess(data,(99.0,20.0),30,120)

# num.cumulativegraph(data,(1,1),120)
num.probabilitygraph(data,(1,1),120)
'''
data = num.wineset2()
print num.crossvalidate(num.weightedknn,data)

data = num.preprocess(data)
print num.crossvalidate(num.weightedknn,data)













