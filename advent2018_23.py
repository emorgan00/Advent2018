import math

bots = []
f = open('input.txt','r')
for line in f.readlines():
	line = line.split(', r=')
	bots.append((map(int,line[0][5:-1].split(',')), int(line[1])))
f.close()

mindist = float('inf')
minx, maxx, miny, maxy, minz, maxz = 0, 0, 0, 0, 0, 0

for b in bots:
	minx = min(minx,b[0][0])
	maxx = max(maxx,b[0][0])
	miny = min(miny,b[0][1])
	maxy = max(maxy,b[0][1])
	minz = min(minz,b[0][2])
	maxz = max(maxz,b[0][2])
	mindist = min(mindist,b[1])

def inrange(pos,bot):
	return abs(pos[0]-bot[0][0])+abs(pos[1]-bot[0][1])+abs(pos[2]-bot[0][2]) <= bot[1]

def ninrange(pos):
	c = 0
	for b in bots:
		if inrange(pos,b): c += 1
	return c

while mindist > 0:
	loc = {}
	print mindist
	offset = mindist*9/11

	for x in xrange(minx-offset,maxx+1,mindist):
		for y in xrange(miny-offset,maxy+1,mindist):
			for z in xrange(minz-offset,maxz+1,mindist):
				loc[(x,y,z)] = ninrange((x,y,z))

	m = max(loc.values())

	opt = []
	for k in loc.keys():
		if loc[k] == m:
			opt.append(k)
	nearest = sorted(opt,key = sum)[0]

	mindist /= 2
	minx = (minx+nearest[0])/2
	maxx = (maxx+nearest[0])/2
	miny = (miny+nearest[1])/2
	maxy = (maxy+nearest[1])/2
	minz = (minz+nearest[2])/2
	maxz = (maxz+nearest[2])/2

	if mindist == 0: 
		break

print nearest,sum(nearest),m