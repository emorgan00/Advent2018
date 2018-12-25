import time, sys, os
f = open('input.txt','r')
data = map(lambda x:list(x.strip().split(' ')[0]),f.readlines())
f.close()

units = []

class Unit:
	def __init__(self,t,x,y):
		self.health = 200
		self.alive = True
		self.power = 25 if t == 'E' else 3
		self.t = t
		self.x = x
		self.y = y

def adj(x,y): return [(a+x,b+y) for a,b in [(0,-1),(-1,0),(1,0),(0,1)]]
def valid(l,f): return filter(lambda p:p[1]>0 and p[0]>0 and p[1]<len(data) and p[0]<len(data[0]) and data[p[1]][p[0]] in f,l)
def inv(s): return 'E' if s=='G' else 'G'

def getunit(p):
	for u in units:
		if u.alive and u.x==p[0] and u.y==p[1]:
			return u
	return None

def nearest(unit):
	seen = set()
	nex = [(unit.x,unit.y)]
	tmap = []
	for line in data:
		tmap.append(map(lambda t:t=='.',line))
	tmap[unit.y][unit.x] = -1
	i = 0
	f = '.'+inv(unit.t)
	while nex:
		i += 1
		sto = []
		seen.update(nex)
		nex.sort(key=(lambda p:(p[1],p[0])))
		for r in map(lambda u:valid(adj(u[0],u[1]),f),nex):
			for t in filter(lambda k:k not in seen,r):
				tmap[t[1]][t[0]] = i
				if t not in sto: sto.append(t)
				if data[t[1]][t[0]] in 'EG': 
					return getunit(t)
		nex = sto
	return None # no enemy is accessible

def direction(unit,target):
	seen = set()
	nex = [(target.x,target.y)]
	tmap = []
	scores = [0,0,0,0]
	for line in data:
		tmap.append(map(lambda t:t=='.',line))
	tmap[target.y][target.x] = -1
	i = 0
	while sum(scores)==0:
		i += 1
		sto = []
		seen.update(nex)
		for r in map(lambda u:valid(adj(u[0],u[1]),'.'),nex):
			for t in filter(lambda k:k not in seen,r):
				tmap[t[1]][t[0]] = i
				if t not in sto: sto.append(t)
				if t[0]==unit.x and t[1]==unit.y-1: scores[0] = 1
				elif t[0]==unit.x-1 and t[1]==unit.y: scores[1] = 1
				elif t[0]==unit.x+1 and t[1]==unit.y: scores[2] = 1
				elif t[0]==unit.x and t[1]==unit.y+1: scores[3] = 1
		nex = sto
	if scores[0]==1: return (unit.x,unit.y-1)
	elif scores[1]==1: return (unit.x-1,unit.y)
	elif scores[2]==1: return (unit.x+1,unit.y)
	elif scores[3]==1: return (unit.x,unit.y+1)
	return None

for y in xrange(len(data)):
	for x in xrange(len(data[0])):
		if data[y][x] not in 'EG': continue
		units.append(Unit(data[y][x],x,y))

def c(ch):
	if ch == '#': return '#'
	elif ch == '.': return ' '
	elif ch == 'G': return '\033[0;32mG\033[0;0m'
	elif ch == 'E': return '\033[0;31mE\033[0;0m'

rnd = 0; flag = True
while flag:
	sys.stdout.write('\n'.join(map(lambda x: ''.join(map(lambda ch: c(ch),x)),data))+'\r')
	time.sleep(0.1)
	units.sort(key=(lambda u:(u.y,u.x)))
	for unit in units:
		if not unit.alive: continue
		if all(unit.t=='G' or not unit.alive for unit in units) or all(unit.t=='E' or not unit.alive for unit in units):
			s = 0
			for u in units:
				if u.t=='E' and not u.alive: print 'FAIL'
				if u.alive: s+=u.health
			print 'OUTPUT',s*rnd
			flag = False
			break
		if not len(valid(adj(unit.x,unit.y),inv(unit.t))):
			target = nearest(unit)
			if target == None: continue
			mx,my = direction(unit,target)
			data[unit.y][unit.x] = '.'
			data[my][mx] = unit.t
			unit.x,unit.y = mx,my
		targets = valid(adj(unit.x,unit.y),inv(unit.t))
		if len(targets)==0: continue
		targets.sort(key=(lambda u:(u[1],u[0])),reverse=True)
		targets = map(getunit,targets)
		target = targets[0]
		for t in targets[1:]:
			if t.health <= target.health: target=t
		target.health -= unit.power
		if target.health <= 0:
			target.alive = False
			data[target.y][target.x] = '.'
	rnd += 1