from random import shuffle

rows = int(input())
cols = int(input())

nums = list(map(str,range(rows * cols)))
shuffle(nums)

print(rows)
print(cols)
for row in range(rows):
	print(" ".join(nums[row * cols:row * cols + cols]))
