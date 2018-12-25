f = open('input.txt','r')
maps = {}

pots = f.readline().strip()[15:]
pots = '.'*100+pots+'.'*300

for line in f.readlines()[1:]:
	d = line.strip().split(' => ')
	maps[d[0]] = d[1]

f.close()

for i in xrange(202):
	out = ''
	for ind in xrange(len(pots)-5):
		out += maps[pots[ind:ind+5]] if pots[ind:ind+5] in maps else '.'
	pots = '.'*2+out+'.'*3
	print i+1,sum((c-100) if pots[c]=='#' else 0 for c in xrange(len(pots)))

print 80*49999999999+946



