input()
l=list(map(int,input().split()))
o=[]
exec("o=[min(l)]+o[::-1];l.remove(min(l));"*len(l))
print(" ".join(map(str,o[::[-1,1][len(o)%2]])))
