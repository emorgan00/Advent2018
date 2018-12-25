f = open('input.txt','r')
data = []
for line in f.readlines():
	data.append(list(line.strip()))
f.close()

def get(x,y):
	if x < 0 or y < 0 or x > 49 or y > 49:
		return '.'
	return data[y][x]

s = {}
for i in xrange(2120): # pulled this number out of my ass
	key = ''.join(map(lambda s:''.join(s),data))
	if key in s.keys() and s[key] == 478: print i,s[key] # identifying patterns in the data
	else: s[key] = i
	new = []
	for y in xrange(50):
		newline = []
		for x in xrange(50):
			ch = data[y][x]
			adj = [get(x+ax,y+ay) for (ax,ay) in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]]
			if ch=='.' and sum(t=='|' for t in adj) > 2:
				ch = '|'
			elif ch=='|' and sum(t=='#' for t in adj) > 2:
				ch = '#'
			elif ch=='#':
				if not (sum(t=='#' for t in adj) > 0 and sum(t=='|' for t in adj) > 0):
					ch = '.'
			newline.append(ch)
		new.append(newline)
	data = new

a,b = 0,0
for x in xrange(50):
	for y in xrange(50):
		if data[y][x] == '|': a+=1
		if data[y][x] == '#': b+=1

print a*b