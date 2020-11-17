n=eval(input("numarul n="))
s11=0
s21=0
r21=0
for i in range(1,(n+1)):
    s11+=i**3
    r21+=i
    s21=r21**2
if s11>s21:
    print("s11 este mai mare secat s21")
if s11<s21:
    print("s11 este mai mic decat s21")
if s11==s21:
    print("s11 este egal cu s21")

n=eval(input("numarul n="))
s12=0
r12=0
s22=0
r22=0
t22=0
for i in range(1,(n+1)):
    r12+=i**2
    s12=3*r12
    r22+=i
    s22=n**3+n**2+r22
if s12>s22:
    print("s12 este mai mare decat s22")
if s12<s22:
    print("s12 este mai mic decat s22")
if s12==s22:
    print("s12 este egal cu s22")