from math import log
f=lambda k,x=1:exec("x=(x+log(k))/(1+log(x));"*9)or x
