def solver(input_list, n):
	if n < 3:
		return input_list[n]
	for _ in range(n-2):
		input_list = input_list[-2:] + [sum(input_list)]
	return input_list[-1]

if __name__ == "__main__":
	n = int(input())
	seq_start = list(map(int, input().split()))
	print(solver(seq_start, n))
