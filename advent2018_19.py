f = open('input.txt','r')
data = []
for line in f.readlines()[1:]:
	data.append(line.strip().split())
f.close()

codes = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']

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

state,pointer = [1, 3, 3, 10551387/3-3, 10551387, 0], 3
ip = 2
i = 0
flag = False
while True:

	state[ip] = pointer
	print str(state)+',',pointer; i+=1
	if pointer >= len(data): 
		print 'done!'
		break
	op(state,data[pointer])
	pointer = state[ip]+1
	if i > 1000: break # testing purposes

print sum([1, 3, 7, 11, 21, 33, 77, 231, 45677, 137031, 319739, 502447, 959217, 1507341, 3517129, 10551387]) # prime factors of 10551387 !!!!!