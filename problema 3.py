from math import log
m=int(input("valoarea lui m-"))
n=int(input("valoarea lui n-"))
i=log(n,m)
l=int(i)
if i-l==0:
    print("n este puterea lui m")
else:
    print("n nu este puterea lui m")