f = open('input.txt','r')
regex = f.read()[1:-1]
f.close()

visits = {}
score = 0

def traverse(s):
	global visits
	x,y,i = 0,0,0
	for c in s:
		if c == 'N': y += 1
		elif c == 'S': y -= 1
		elif c == 'E': x += 1
		elif c == 'W': x -= 1
		i += 1
		if (x,y) in visits and visits[(x,y)] < i:
			i = visits[(x,y)]
		else:
			visits[(x,y)] = i

def solve(pre,s):
	for op in partition(s):
		if '(' in op:
			oi = op.index("(")
			c = 0
			for i in range(oi,len(op)):
				if op[i] == '(': c += 1
				if op[i] == ')': c -= 1
				if c == 0:
					ci = i+1
					break
			solve(pre+op[:oi],op[oi+1:ci-1]+op[ci:])
		else:
			traverse(pre+op)

def partition(s):
	out = []
	sto = ''
	dep = 0
	for c in s:
		if c == '(': dep += 1; sto += c
		elif c == ')': dep -= 1; sto += c
		elif c == '|' and dep == 0: yield sto; sto = ''
		else: sto += c
	yield sto

solve('',regex)
print 'part 1:',max(visits.values())
k = 0
for i in visits.values():
	if i > 999: k += 1
print 'part 2:',k