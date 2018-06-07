import math
from PIL import Image,ImageDraw

people = ['Charlie','Augustus','Veruca','Violet','Mike','Joe','Willy','Miranda']

links = [('Augustus','Willy'),('Mike','Joe'),('Miranda','Mike'),('Violet','Augustus'),('Miranda','Willy'),('Charlie','Mike'),('Veruca','Joe'),('Miranda','Augustus'),('Willy','Augustus'),('Joe','Charlie'),('Veruca','Augustus'),('Miranda','Joe')]

domain = [(10,370)]*len(people)*2

def crosscount(v):
    loc = dict([(people[i], (v[i*2],v[i*2+1])) for i in range(0,len(people))])
    total = 0
    for i in range(len(links)):
        for j in range(i+1,len(links)):
            (x1,y1),(x2,y2) = loc[links[i][0]], loc[links[i][1]]
            (x3,y3),(x4,y4) = loc[links[j][0]], loc[links[j][1]]
            den = (y3-y4)*(x1-x2) - (x3-x4)*(y1-y2)
            if den == 0: continue
            x = ((x3-x4)*(x1*y2-x2*y1)-(x1-x2)*(x3*y4-x4*y3))/den
            if (x - x1)*(x - x2) < 0:
                total += 1
            dist = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            if dist < 50.0:
                total += (1.0-dist/50.0)*5
            dist = math.sqrt(math.pow(x3-x4,2)+math.pow(y3-y4,2))
            if dist < 50.0:
                total += (1.0-dist/50.0)*5
    return total

def drawnetwork(sol):
    img = Image.new('RGB',(400,400),(255,255,255))
    draw = ImageDraw.Draw(img)
    pos = dict([(people[i], (sol[i*2],sol[i*2+1])) for i in range(0,len(people))])
    for (a,b) in links:
        draw.line((pos[a],pos[b]), fill=(255,0,0))
    for n,p in pos.items():
        draw.text(p,n,(0,0,0))
    img.show()
