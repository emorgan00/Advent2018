grps = []
f = open('input.txt','r')
for line in f.readlines():
	s = map(int,line.split(','))
	mem = filter(lambda g: any(sum(abs(a-b) for a, b in zip(s, st)) < 4 for st in g), grps)
	if len(mem) == 0: grps.append([s])
	else:
		mem[0].append(s)
		for oth in mem[1:]:
			mem[0] += oth
			grps.remove(oth)
print len(grps)
f.close()