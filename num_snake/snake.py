rows = int(input())
cols = int(input())

board = []
seen = []
for i in range(rows):
	board.append(list(map(int, input().split())))
	seen.append([0] * len(board[-1]))

global_best = 0

def solver(x, y, count, score, path, seen, values, rows, cols):
	global global_best
	if count == rows * cols:
		return score, path
	if x < 0 or y < 0 or y >= rows or x >= cols:
		return None
	if seen[y][x] == 1:
		return None
	if global_best and score > global_best:
		return None
	seen[y][x] = 1
	solns = [solver(x, y-1, count+1, score + values[y][x] * count, path + "U", seen, values, rows, cols)]
	solns.append(solver(x, y+1, count+1, score + values[y][x] * count, path + "D", seen, values, rows, cols))
	solns.append(solver(x-1, y, count+1, score + values[y][x] * count, path + "L", seen, values, rows, cols))
	solns.append(solver(x+1, y, count+1, score + values[y][x] * count, path + "R", seen, values, rows, cols))
	solns = [x for x in solns if x]
	seen[y][x] = 0
	if solns:
		if not global_best or min(solns)[0] <= global_best:
			global_best = min(solns)[0]
			print("Best so far- {} {}".format(*min(solns)))
		return min(solns)
	return None

val, path = solver(0, 0, 0, 0, "", seen, board, rows, cols)
print(val, path[:-1])
