n=float(input())
v=0
for i in 1,1e-6:
 while v**v<n:v+=i
 v-=i
print(round(v,5))
