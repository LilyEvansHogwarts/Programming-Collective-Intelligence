from recommendations import *
import time

prefs = loadMovieLens()
itemMatch = calculateSimilarItems(prefs, n=50)

start = time.clock()
items = getRecommendations(prefs, '87', similarity=sim_tanimoto)[0:30]
end = time.clock()
print items
print 'Running Time:', end-start

start = time.clock()
items = getRecommendedItems(prefs, itemMatch, '87')[0:30]
end = time.clock()
print items
print 'Running Time:', end-start

