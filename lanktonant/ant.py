from random import choice, randint

def rand(size):
	s = ""
	for _ in range(size):
		s += choice("#.")
	return s

def gen_map(size):
	direction = choice("NSEW")
	x = randint(0, size-1)
	y = randint(0, size-1)
	
	tiles1 = "\n".join([rand(size + 1) for _ in range(size)])
	tiles2 = "\n".join([rand(size + 1) for _ in range(size)])
	return "{}\n{} {}\n{} {}\n{}\n{}".format(direction, x, y, size, size + 1, tiles1, tiles2)


for i, size in enumerate([15, 20]):
	with open("py_test{}.txt".format(size), "w") as file:
		file.write(gen_map(size))
