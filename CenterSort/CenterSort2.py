input()
l=sorted(input().split(),key=int)
print(" ".join(l[::2][::-1]+l[1::2]))
