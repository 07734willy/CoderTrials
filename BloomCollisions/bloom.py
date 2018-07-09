def h1(n):
	#return (n * 792641) >> 32
	#return (n * 65521) >> 64
	return n % 65521

def h2(n):
	return ((n * 2654435769) >> 16) & 0xFFFF
	#return (n * 40503) & 0xFFFF

def h3(n):
	return ((n * 11400714819323198485) >> 48) & 0xFFFF

"""
elems = set()
for i in range(100):
	#a = 7778742049*65521 * i
	a = 65521 * i
	print(a,h1(a),h3(a))
	elems.add(h1(a))
	elems.add(h2(a))

print(len(elems))
print(",".join(map(str,[i * 65521 for i in range(100)])))
"""
r = {x for x in range(10)}
i = 0
out = set()
"""
while i < 2**32:
	if h3(i) == 3:
		print("HI")
	i += 65521
print(len(out))
"""
c = 1
for i in range(2**24):
	c+=1
print(c)
"""
from collections import defaultdict
d = defaultdict(int)
for j in range(20):
	for i in range(j, 2**32, 65521):
		a = h1(i)
		b = h2(i)
		d[(min(a,b),max(a,b))] += 1

#print(sorted(zip(d.values(),d.keys()))[:10])
"""
