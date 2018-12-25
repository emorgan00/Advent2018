from heapq import *

depth = 7863
tx,ty = 14, 760

sx, sy, data = tx+100, ty+100, {}

def index(x,y):
	if (x==0 and y==0) or (x==tx and y==ty): out = 0
	elif (y==0): out = x*16807
	elif (x==0): out = y*48271
	else: out = (data[(x-1,y)]+depth)%20183*(data[(x,y-1)]+depth)%20183
	return out

for y in xrange(sy+1):
	for x in xrange(sx+1):
		data[(x,y)] = index(x,y)
for key in data.keys(): data[key] = (data[key]+depth)%20183%3

inf = float('inf')
distance, queue = {(0, 0): (inf, 0, 7)}, [(0, 0)]

while queue:
	x, y = heappop(queue)
	d = data.get((x,y), -1)
	if x < 0 or y < 0 or x > sx or y > sy: continue
	n, t, c = distance.get((x, y), (inf, inf, inf))
	for loc in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
		nn, nt, nc = distance.get(loc, (inf, inf, inf))
		nd = data.get(loc, -1)
		nn = inf if nd == 0 else min(nn, inf if d == 0 else min(n+1, t+8, c+8))
		nt = inf if nd == 1 else min(nt, inf if d == 1 else min(n+8, t+1, c+8))
		nc = inf if nd == 2 else min(nc, inf if d == 2 else min(n+8, t+8, c+1))
		if (nn, nt, nc) < distance.get(loc, (inf, inf, inf)):
			distance[loc] = (nn, nt, nc)
			heappush(queue, loc)

print distance[(tx,ty)][1]