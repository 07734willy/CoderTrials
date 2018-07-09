
from collections import defaultdict
from itertools import combinations_with_replacement as combwr
from random import sample

def hash1(n):
	return n % 65521

def hash2(n):
	return ((n * 11400714819323198485) >> 48) & 0xFFFF

mSize = 200
canidates = []
h1 = 0
i = 0
while i < 2**32:
	if h1 < mSize:
		h2 = hash2(i)
		if h2 < mSize:
			canidates.append((i, (h1, h2)))
	h1 += 1
	if h1 == mSize:
		h1 = 0
		i += 65322
	else:
		i += 1

print(len(canidates))

soln1 = [(190, 190), (149, 190), (149, 149), (92, 190), (92, 149), (92, 92), (92, 105), (92, 99), (92, 143), (71, 190), (71, 149), (71, 92), (71, 71), (71, 105), (71, 99), (71, 143), (105, 190), (105, 149), (105, 105), (105, 143), (99, 190), (99, 149), (99, 105), (99, 99), (99, 143), (11, 190), (11, 149), (11, 92), (11, 71), (11, 105), (11, 99), (11, 11), (11, 143), (11, 41), (143, 190), (143, 149), (143, 143), (41, 190), (41, 149), (41, 92), (41, 71), (41, 105), (41, 99), (41, 143), (41, 41)]
solnIdx = []

d = defaultdict(int)
for idx, (h1, h2) in canidates:
	d[(min(h1,h2),max(h1,h2))] += 1
	if (min(h1,h2),max(h1,h2)) in soln1:
		solnIdx.append(idx)

print(solnIdx)


print(sorted(zip(d.values(),d.keys()))[-10:])

vals = list(zip(*d.keys()))[0]+list(zip(*d.keys()))[1]
counts = [(vals.count(i),i) for i in range(mSize)]

topSize = 100
top = sorted(counts)[-topSize:]
#top = sorted(counts)
tvals = sorted(list(zip(*top))[1])
#print(top)

outLast = []
sizeLast = 0
size = 10
#for comb in combwr(tvals, size):
while True:
	comb = sample(tvals, size)
	c = 0
	out = []
	for v1 in comb:
		for v2 in comb:
			if c >= 100:
				break
			if v1 > v2:
				continue
			tup = (min(v1,v2),max(v1,v2))
			if tup in d:
				c += d[tup]
				out.append(tup)
		if c >= 100:
			break
	if c >= 100:
		print("success")
		if sizeLast == 0 or size < sizeLast:
			print(size)
			outLast = list(out)
			sizeLast = size
			size -= 1
			print(outLast)
print(outLast)











"""
success = True
outLast = []
idx = -40
while success:
	top = sorted(counts)[idx:]
	tvals = list(zip(*top))[1]
	success = False
	c = 0
	out = []
	for v1 in tvals:
		for v2 in tvals:
			if v1 > v2:
				continue
			tup = (min(v1,v2),max(v1,v2))
			if tup in d:
				c += d[tup]
				out.append(tup)
	if c >= 100:
		print("success at {}".format(idx))
		success = True
	idx += 1
	outLast = list(out)
print(outLast)
"""
