from random import randint
import sys

size = int(input())
span = int(input())

values = set()
while len(values) < size:
	values.add(randint(-span,span))

print(size)
print(" ".join(map(str,values)))
print(size,file=sys.stderr)
print(" ".join(map(str,values)),file=sys.stderr)
