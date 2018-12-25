f = open('input.txt','r')

data = []
for line in f.readlines():
	d = list(line[:-1])
	while len(d) < 160:
		d.append(' ')
	data.append(d)

f.close()
for line in data: print ''.join(line)
carts = []
tiles = {}
for x in xrange(160):
	for y in xrange(len(data)):
		if data[y][x] in '^v':
			carts.append([x-y*1j,0+1j if data[y][x] == '^' else 0-1j,0])
			data[y][x] = '|'
		if data[y][x] in '<>':
			carts.append([x-y*1j,-1+0j if data[y][x] == '<' else 1+0j,0])
			data[y][x] = '-'
		if data[y][x] in '\\/+':
			tiles[x-y*1j] = data[y][x]
queue = []
tset = set(tiles.keys())
while len(carts) != 1:
	for c in sorted(carts, key = lambda x: (-x[0].imag, x[0].real)):

		c[0] += c[1] # motion
		t = tiles[c[0]] if c[0] in tset else ' ' # new tile we are sitting on

		if t == '\\':
			if int(c[1].real) == 0: c[1] *= 1j
			else: c[1] *= -1j
		elif t == '/':
			if int(c[1].real) == 0: c[1] *= -1j
			else: c[1] *= 1j
		elif t == '+':
			if c[2]%3 == 0:
				c[1] *= 1j
			elif c[2]%3 == 2:
				c[1] *= -1j
			c[2] += 1

		for c1 in carts:
			if c[0] == c1[0] and c[2] != c1[2]:
				print 'crash at',c
				queue.append(c)
				queue.append(c1)
	while len(queue) > 0:
		carts.remove(queue.pop())

print carts[0][0]