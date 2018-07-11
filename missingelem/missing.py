i=input
i()
o=i().split()
s=set(o)-set(i().split())
r=[x for x in o if x in s];print(r[:len(s)>1]+r[-1:])
#print([x for x in o if x in s][::len(s)-1] if len(s)>1 else "".join(s))
