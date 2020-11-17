a=int(input("prima latura="))
b=int(input("a doua latura="))
c=int(input("a treia latura="))
if ((a==b)or(a==c)or(b==c)):
    print("triunghi isoscel")
if((a==b)and(b==c)):
    print("triunghi echilateral")
if((a!=b)and(b!=c)and(a!=c)):
    print("triunghi scalen")