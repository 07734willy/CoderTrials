from itertools import permutations

size = int(input())
vals = list(map(int,input().split()))

solutions = set()
for x, y in permutations(vals, 2):
	z = -x - y
	if z in vals:
		solutions.add(tuple(sorted([x, y, z])))
for soln in solutions:
	print("{}, {}, {}".format(*soln))
