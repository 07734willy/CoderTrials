s=int(input())
r=""
c=0
f=lambda x:(x%3**i)//3**(i-1)
exec('t="#";i=1;exec(\'t=[t," "][f(c)*f(c//3**s)==1];i+=1;\'*s);c+=1;r+=t;r+="\\n"*(c%3**s<1);'*9**s)
print(r)
