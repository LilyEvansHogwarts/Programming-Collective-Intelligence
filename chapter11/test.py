from gp import *
'''
exampletree = exampletree()

print exampletree.evaluate([2,3])
print exampletree.evaluate([5,3])

print
exampletree.display()

print
random1 = makerandomtree(2)
random1.display()

print
print random1.evaluate([7,1])
print random1.evaluate([2,4])

print
random2 = makerandomtree(2)
random2.display()
print 
print random2.evaluate([5,3])
print random2.evaluate([5,20])
'''
rf = getrankfunction(buildhiddenset())
tree = evolve(2,500,rf,mutationrate=0.2,breedingrate=0.1)
tree.display()
print
newtree = simplify(tree)
newtree.display()


'''
tree = node(ifw,[node(gtw,[constnode(1),constnode(0)]),
    node(addw,[paramnode(0),constnode(1)]),
    node(subw,[paramnode(1),constnode(3)])])

tree.display()
# tree = node(gtw,[constnode(1),constnode(3)])
newtree = simplify(tree)
newtree.display()
'''

