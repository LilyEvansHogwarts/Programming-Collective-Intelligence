import advancedclassify as ad
import treepredict as tr

agesonly = ad.loadmatch('agesonly.csv',allnum=True)
matchmaker = ad.loadmatch('matchmaker.csv')

ad.plotagematches(agesonly)

age = []
for line in file('agesonly.csv'):
    l = []
    for w in line.split(','):
        l.append(int(w))
    age.append(l)
tree = tr.buildtree(age)
tr.printtree(tree)
tr.drawtree(tree)
