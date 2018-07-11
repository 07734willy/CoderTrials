from random import randint,shuffle

def gen(size, lower, upper, missing):
	orig = [randint(lower, upper) for _ in range(size)]
	drop = list(orig)
	shuffle(orig)
	new = drop[:size-missing]
	dropped = drop[size-missing:]
	print("{} {}".format(len(orig), len(new)))
	print(" ".join(map(str,orig)))
	print(" ".join(map(str,new)))
	print("")
	print(" ".join(map(str,dropped)))
	print("")


gen(6, 0, 20, 3)
gen(10, 0, 20, 5)
gen(12, -10, 10, 6)
gen(25, 0, 200, 10)
