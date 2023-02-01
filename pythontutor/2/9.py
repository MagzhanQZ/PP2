a=int(input())
b=int(input())
c=int(input())
d=int(input())

if ((b-a)%2==0 and (d-c)%2==0) or ((b-a)%2==1 and (d-c)%2==1):
    print("YES")
else:
    print("NO")