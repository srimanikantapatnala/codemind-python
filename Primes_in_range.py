def prime(n):
    fc=0
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
            fc=fc+1
    return(fc==0)
s=0
m=int(input())
n=int(input())
for i in range(m,n+1):
    if prime(i)==True:
        s+=1
print(s)