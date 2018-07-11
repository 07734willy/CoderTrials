def m(s):
 if s<1:return["#"]
 r=m(s-1)
 x=r*3
 y=r+[" "*len(r)]*len(r)+r
 return list(map("".join,zip(x,y,x)))
print("\n".join(m(int(input()))))
