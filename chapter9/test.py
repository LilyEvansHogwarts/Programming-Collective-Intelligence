import advancedclassify as ad
import treepredict as tr

agesonly = ad.loadmatch('agesonly.csv',allnum=True)
matchmaker = ad.loadmatch('matchmaker.csv')

# ad.plotagematches(agesonly)

age = []
for line in file('agesonly.csv'):
    l = []
    for w in line.split(','):
        l.append(int(w))
    age.append(l)
tree = tr.buildtree(age)
tr.printtree(tree)
tr.drawtree(tree)

print tr.classify(tree,[65,63])


avgs = ad.lineartrain(agesonly)
print avgs

print ad.dpclassify([30,25],avgs.values())
print ad.dpclassify([25,40],avgs.values())
print ad.dpclassify([48,20],avgs.values())

print tr.classify(tree,[30,25])
print tr.classify(tree,[25,40])
print tr.classify(tree,[48,20])

numericalset = ad.loadnumerical()
numericalset[0].data
