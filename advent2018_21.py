s = set()
upper = 65536
test = 1397714
while True:
	test = (((test+(255&upper))&16777215)*65899)&16777215
	if 256 > upper:
		if test in s:
			print 'answer is the last value above' 
			break
		else:
			print test
			s.add(test)
		upper = test | 65536
		test = 1397714
	else: upper /= 256