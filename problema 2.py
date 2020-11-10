n=int(input("introduceti valoarea n-"))
s=0
factorial=1
while n>1:
    factorial*=n
    n=1
    s+=factorial

print("suma factorialelor de la 1 la n=",s)