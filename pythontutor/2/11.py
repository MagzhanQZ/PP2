a=int(input())
b=int(input())
c=int(input())
d=int(input())

if (((a-1==c) or (a+1==c)) and ((b+2==d)or(b-2==d))) or (((a-2==c) or (a+2==c)) and ((b+1==d)or(b-1==d))):
    print("YES")
else:
    print("NO")