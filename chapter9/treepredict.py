from PIL import Image,ImageDraw

def divideset(rows,column,value):
    split_function = None
    if isinstance(value,int) or isinstance(value,float):
        split_function = lambda row:row[column]>=value
    else:
        split_function = lambda row:row[column]==value
    set1 = [row for row in rows if split_function(row)]
    set2 = [row for row in rows if not split_function(row)]
    return (set1,set2)

def uniquecounts(rows):
    results = {}
    for row in rows:
        r = row[len(row)-1]
        results.setdefault(r,0)
        results[r] += 1
    return results

def giniimpurity(rows):
    total = len(rows)
    counts = uniquecounts(rows)
    imp = 0.0
    for k1 in counts:
        p1 = float(counts[k1])/total
        for k2 in counts:
            if k1 == k2: continue
            p2 = float(counts[k2])/total
            imp += p1*p2
    return imp

def entropy(rows):
    from math import log
    log2 = lambda x:log(x)/log(2)
    results = uniquecounts(rows)
    ent = 0.0
    total = len(rows)
    for k in results.values():
        r = float(k)/total
        ent -= r*log2(r)
    return ent

def buildtree(rows,scoref=entropy):
    if len(rows) == 0: return decisionnode()
    current_score = scoref(rows)
    best_gain = 0
    best_criteria = None
    best_sets = None
    column_count = len(rows[0])-1
    for col in range(column_count):
        column_values = {}
        for row in rows:
            column_values[row[col]] = 1
        for value in column_values:
            (set1,set2) = divideset(rows,col,value)
            p = float(len(set1))/len(rows)
            gain = current_score-p*scoref(set1)-(1-p)*scoref(set2)
            if gain>best_gain:
                best_gain = gain
                best_criteria = (col,value)
                best_set = (set1,set2)
    if best_gain>0:
        trueBranch = buildtree(best_set[0],scoref)
        falseBranch = buildtree(best_set[1],scoref)
        return decisionnode(col=best_criteria[0],value=best_criteria[1],tb=trueBranch,fb=falseBranch)
    else:
        return decisionnode(results=uniquecounts(rows))

def printtree(tree,indent=''):
    if tree.results != None:
        print str(tree.results)
    else:
        print str(tree.col)+':'+str(tree.value)+'?'
        print indent+'T->',
        printtree(tree.tb,indent+'  ')
        print indent+'F->',
        printtree(tree.fb,indent+'  ')

def getwidth(tree):
    if tree.tb == None and tree.fb == None: return 1
    return getwidth(tree.tb)+getwidth(tree.fb)

def getdepth(tree):
    if tree.tb == None and tree.fb == None: return 0
    return max(getdepth(tree.tb),getdepth(tree.fb))+1

def drawtree(tree,jpeg='tree.jpg'):
    w = getwidth(tree)*50
    h = getdepth(tree)*50+200
    img = Image.new('RGB',(w,h),(255,255,255))
    draw = ImageDraw.Draw(img)
    drawnode(draw,tree,w/2,20)
    img.save(jpeg,'JPEG')

def drawnode(draw,tree,x,y):
    if tree.results == None:
        w1 = getwidth(tree.fb)*50
        w2 = getwidth(tree.tb)*50
        draw.text((x-20,y-10),str(tree.col)+':'+str(tree.value),(0,0,0))
        draw.line((x,y,x-w2/2,y+50),fill=(255,0,0))
        draw.line((x,y,x+w1/2,y+50),fill=(255,0,0))

        drawnode(draw,tree.fb,x-w2/2,y+50)
        drawnode(draw,tree.tb,x+w1/2,y+50)
    else:
        txt = ' \n'.join(['%s:%d'%v for v in tree.results.items()])
        draw.text((x-20,y),txt,(0,0,0))

class decisionnode:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb






        
