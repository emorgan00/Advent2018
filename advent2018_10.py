f = open('input.txt','r')
pos, vel = [], []
for line in f.readlines():
	pos.append([int(line[10:16]),int(line[18:24])])
	vel.append((int(line[36:38]),int(line[40:42])))
f.close()
s = 0
while True:
	for i in xrange(len(pos)):
		pos[i][0] += vel[i][0]
		pos[i][1] += vel[i][1]
	if all(k[1] > -200 and k[1] < 200 for k in pos):
		output = [['.' for i in xrange(1000)] for j in xrange(400)]
		for p in pos:
			output[200+p[1]][200+p[0]] = '@'
		for l in output:
			if '@' in l:
				print str(s)+' '+(''.join(l))
		print '\n'
	s += 1
# EKALLKLB
