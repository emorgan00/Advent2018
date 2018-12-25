f = open('input.txt','r')
sto = []
i = 0
data = []
for line in f.readlines():
	if line[0] == '#': break
	if i==3: 
		data.append(sto)
		sto = []
	elif i==0:
		sto.append(map(int,line.strip()[line.index('[')+1:line.index(']')].split(', ')))
	elif i==2:
		sto.append(map(int,line.strip()[line.index('[')+1:line.index(']')].split(', ')))
	else:
		sto.append(map(int,line.strip().split(' ')))
	i = (i+1)%4
f.close()

codes = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']
maps = {}
for code in codes:
	maps[code] = set(range(16))

def op(state,line):
	code,a,b,c = line[0],int(line[1]),int(line[2]),int(line[3])
	if   code == 'addr': state[c] = state[a] + state[b]
	elif code == 'addi': state[c] = state[a] + b
	elif code == 'mulr': state[c] = state[a] * state[b]
	elif code == 'muli': state[c] = state[a] * b
	elif code == 'banr': state[c] = state[a] & state[b]
	elif code == 'bani': state[c] = state[a] & b
	elif code == 'borr': state[c] = state[a] | state[b]
	elif code == 'bori': state[c] = state[a] | b
	elif code == 'setr': state[c] = state[a]
	elif code == 'seti': state[c] = a
	elif code == 'gtir': state[c] = 1 if a > state[b] else 0
	elif code == 'gtri': state[c] = 1 if state[a] > b else 0
	elif code == 'gtrr': state[c] = 1 if state[a] > state[b] else 0
	elif code == 'eqir': state[c] = 1 if a == state[b] else 0
	elif code == 'eqri': state[c] = 1 if state[a] == b else 0
	elif code == 'eqrr': state[c] = 1 if state[a] == state[b] else 0
	return state

while any(len(maps[key]) > 1 for key in codes):
	for test in data:
		for code in codes:
			if not op(test[0][:],[code]+test[1][1:]) == test[2]:
				val = test[1][0]
				if val in maps[code]: maps[code].remove(val)
	for code in codes:
		if len(maps[code])==1:
			val = list(maps[code])[0]
			for rm in codes:
				if rm != code and val in maps[rm]: maps[rm].remove(val)
for code in codes:
	print code,list(maps[code])[0]
	maps[code] = list(maps[code])[0]
	maps[maps[code]] = code

f = open('input.txt','r')
while f.readline()[0] != '#': pass
f.readline()

state = [0, 0, 0, 0]
for line in f.readlines():
	line = map(int,line.strip().split(' '))
	print [maps[line[0]]]+line[1:]
	op(state,[maps[line[0]]]+line[1:])

print state

f.close()
