import treepredict as tr

tree = tr.buildtree(tr.my_data)
tr.printtree(tree)
print tr.mdclassify(['google',None,'yes',None],tree)
print tr.mdclassify(['google','France',None,None],tree)
