n=int(input("varsta lui Mihai="))
c=1
if n<20:
    for i in range(1,n+1):
        if (i==n):
            c=c+2
        else:
            c=(c*2)+i

print("la varsta de",n,"ani Mihai a primit",c,"$")
print("cadoul lui mihai a fost mai mare de 100$ la 6 ani")
