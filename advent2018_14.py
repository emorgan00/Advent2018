
def main():
	data = [3, 7]

	e = 0
	f = 1

	r = 760221
	sr = str(r)
	lr = map(int,list(sr))

	while True:
		s = str(data[e] + data[f])
		for c in s:
			c = int(c)
			data.append(c)
		for j in xrange(len(data)-len(s)-len(sr),len(data)-len(sr)):
			if data[j:j+len(sr)] == lr:
				return j

		e = (e+data[e]+1)%len(data)
		f = (f+data[f]+1)%len(data)

print main()