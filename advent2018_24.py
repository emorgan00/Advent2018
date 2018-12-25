class Group:
	def __init__(self, typ, units, hp, im, we, atk, atkt, ini):
		self.units = units
		self.hp = hp
		self.typ = typ
		self.immune = im
		self.weak = we
		self.atk = atk
		self.atktype = atkt
		self.initiative = ini
		self.target = None

	def pow(self): return self.units*self.atk

	def damage(self,other):
		base = 0 if self.atktype in other.immune else self.pow()
		if self.atktype in other.weak: base *= 2
		return base

boost = 35 # setting this to 0 produces the answer for part 1.

f = open('input.txt','r')
groups, typ = [], 0
for line in f.readlines():
	if line[:3] == 'Inf': typ = 1
	if not line[0].isdigit(): continue
	# adding groups
	groups.append(Group(
		typ, int(line.split(' ')[0]), int(line.split(' ')[4]),
		line.split('(')[1].split(')')[0].split(';')[0].split(','),
		line.split('(')[1].split(')')[0].split(';')[1].split(','),
		int(line.split(' ')[13])+(boost if typ == 0 else 0), line.split(' ')[14],
		int(line.split(' ')[-1])))
f.close()

while any(groups[i].typ != groups[i+1].typ for i in xrange(len(groups)-1)):
	# target selection phase
	groups.sort(key = lambda g: (g.pow(), g.initiative), reverse = True)
	chosen = set()
	for group in groups:
		targets = sorted(filter(lambda g: g.typ != group.typ and group.damage(g) != 0 and g not in chosen, groups), key = lambda g: (group.damage(g), g.pow(), g.initiative))
		group.target = targets[-1] if len(targets) > 0 else None
		chosen.add(group.target)
	# attacking phase
	groups.sort(key = lambda g: g.initiative, reverse = True)
	for group in groups:
		if group.units <= 0 or group.target == None: continue
		group.target.units -= group.damage(group.target)/group.target.hp
	groups = filter(lambda g: g.units > 0,groups)

print 'winning side:',['Immune System','Infection'][groups[0].typ]
print 'remaining units:',sum(g.units for g in groups)