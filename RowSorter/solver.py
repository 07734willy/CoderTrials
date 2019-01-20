f=lambda n,m:"\n".join("".join(sorted(r.ljust(max(map(len,m))),key="+ *".index))for r in m)

n=int(input())
m=[input() for _ in range(n)]
print(f(n,m))
