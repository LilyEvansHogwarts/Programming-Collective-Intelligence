import clusters as cl
import numpy as np
import random

blognames, words, data = cl.readfile('blogdata.txt')
'''
clust = cl.hcluster(data)
cl.printclust(clust,labels=blognames)
cl.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

rdata = cl.rotatematrix(data)
wordclust = cl.hcluster(rdata)
cl.printclust(wordclust,labels=words)
cl.drawdendrogram(wordclust,words,jpeg='wordclust.jpg')

k = 4
kclust = cl.kcluster(data,k=k)
l = [[blognames[r] for r in kclust[i]] for i in range(k)]
for ll in l:
    print len(ll),ll


kclust = cl.kcluster_np(data,k=k)
l = [[blognames[r] for r in kclust[i]] for i in range(k)]
for ll in l:
    print len(ll),ll


wants,people,data = cl.readfile('zebo')
clust = cl.hcluster(data,distance=cl.tanimoto)
cl.drawdendrogram(clust,wants)
'''

coords = cl.scaledown(data)
cl.draw2d(coords,blognames,jpeg='blogs2d.jpg')


