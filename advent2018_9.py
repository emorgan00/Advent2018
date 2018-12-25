p = 479 # number of players
l = 71035 # value of largest marble

class Node:
	def __init__(self,val,nex,pre):
		self.val = val
		self.nex = nex
		self.pre = pre

current = Node(0,None,None)
current.nex,current.pre = current,current
c = 1
players = [0 for i in xrange(p)] # scores

for i in [1,2]:

	while c < l+1:
		if i == 2 and c%(l*10) == 0: print str(c//l)+'%...',
		if c%23 == 0 and c != 0:
			a = current.pre.pre.pre.pre.pre.pre.pre.pre
			b = current.pre.pre.pre.pre.pre.pre
			players[c%p] += c+current.pre.pre.pre.pre.pre.pre.pre.val
			current,a.nex,b.pre = b,b,a
		else:
			a,b = current.nex,current.nex.nex
			current = Node(c,b,a)
			a.nex,b.pre = current,current
		c += 1

	print '\nPart %i: %i' % (i, max(players))
	l *= 100

# Note: python tends to be very slow for tasks like this. In java the same program would take about a second.