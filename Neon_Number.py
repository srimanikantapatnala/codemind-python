n=int(input())
sq=n**2
s=0
while sq>0:
    r=sq%10
    s=s+r
    sq=sq//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")
    