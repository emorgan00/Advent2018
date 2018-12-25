import sys
sys.setrecursionlimit(2000) # overkill

f = open('input.txt','r')
maxy,miny = 0,2000
data = [[0]*1000 for y in xrange(2000)]
for line in f.readlines():
	if line[0] == 'x':
		x0 = int(line.split(',')[0][2:])
		x1 = int(x0)
		y0 = int(line.split(' ')[1][2:].split('..')[0])
		y1 = int(line.split(' ')[1][2:].split('..')[1])
	if line[0] == 'y':
		y0 = int(line.split(',')[0][2:])
		y1 = int(y0)
		x0 = int(line.split(' ')[1][2:].split('..')[0])
		x1 = int(line.split(' ')[1][2:].split('..')[1])
	for x in xrange(x0,x1+1):
		for y in xrange(y0,y1+1):
			data[y][x] = 1
	if y1 > maxy: maxy = y1
	if y0 < miny: miny = y0
f.close()

# 0 = sand
# 1 = clay
# 2 = still water
# 3 = moving water

def drop(x,y):
	yi = y
	while y <= maxy and data[y+1][x] == 0:
		y += 1
	for yj in range(yi,y+1)[::-1]:
		if fill(x,yj): finalize(x,yj)

def fill(x,y):
	if y > maxy: return False
	data[y][x] = 3
	if data[y+1][x] == 0:
		drop(x,y+1)
		if data[y+1][x] != 2: return False
	if data[y+1][x] == 3: return False # note the lack of elif here. This conditional is still run if we had to drop
	else:
		if data[y][x-1] == 0 and data[y][x+1] == 0: 
			a = fill(x+1,y)
			b = fill(x-1,y)
			return a and b
		elif data[y][x+1] == 0: return fill(x+1,y)
		elif data[y][x-1] == 0: return fill(x-1,y)
		else: return True

def finalize(x,y): # convert flowing water into still water
	data[y][x] = 2
	if data[y][x+1] == 3: finalize(x+1,y)
	if data[y][x-1] == 3: finalize(x-1,y)

drop(500,0)

c1,c2 = 0,0
for line in data[miny:maxy+1]:
	for ch in line:
		if ch in (2,3): c1 += 1
		if ch == 2: c2 += 1
print 'Part 1: %i\nPart 2: %i' % (c1,c2)