cells = [[((((x+10)*y+2187)*(x+10))//100)%10-5 for x in xrange(300)] for y in xrange(300)]

def get_weight(x,y,s):
	c = 0
	for ox in range(s):
		for oy in range(s):
			c += cells[oy+y][ox+x]
	return c

m = 0
mx,my,s = 0,0,0
#          v,x,y
maxes = [[[0,0,0] for x in xrange(300)] for y in xrange(300)]
maxes[0][0][0] = cells[0][0]
for i in xrange(1.300):
	if maxes[i-1][0][0] < 0:
		maxes[i][0] = [cells[i][0],0,i]
	else:
		maxes[i][0] = [cells[i][0]+maxes[i-1][0][0],maxes[0][i-1][1],maxes[0][i-1][2]]
	if maxes[0][i-1][0] < 0:
		maxes[0][i] = [cells[0][i],0,i]
	else:
		maxes[0][i] = [cells[0][i]+maxes[0][i-1][0],maxes[0][i-1][1],maxes[0][i-1][2]]

for x in xrange(1,300):
	for y in xrange(1,300):
		k = maxes[y][x-1][0]+maxes[y-1][x][0]+maxes[y-1][x-1][0]
		if maxes[y][x-1][2] != y: 
			k -= maxes[y-1][x-1][0]
		if maxes[y-1][x][1] != x: 
			k -= maxes[y-1][x-1][0]
		maxes[y][x] = [cells[y][x],0,0]
		if k < 0:
			maxes[y][x][1],maxes[y][x][2] = x,y
		else:
			maxes[y][x][0] += k
			maxes[y][x][1],maxes[y][x][2] = x,y





