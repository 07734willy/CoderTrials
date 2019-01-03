from itertools import combinations_with_replacement as comb_wr
    
size = int(input())
vals = set(map(int,input().split()))

solutions = set()
for x, y in comb_wr(vals, 2):
	z = -x - y
	if z in vals:
		solutions.add(tuple(sorted([x, y, z])))
for soln in solutions:
	print("{}, {}, {}".format(*soln))
