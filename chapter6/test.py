import docclass as d

cl = d.fisherclassifier(d.getwords)
d.sampletrain(cl)
print cl.classify('quick rabbit')
print cl.classify('quick money')
cl.setminimum('bad',0.8)
print cl.classify('quick money')
cl.setminimum('good',0.4)
print cl.classify('quick money')

for i in range(10): d.sampletrain(cl)
print cl.classify('quick money')

