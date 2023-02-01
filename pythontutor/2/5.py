a=int(input())
b=int(input())
c=int(input())

if a>=b>=c:
    print(c)
elif b>=a>=c:
    print(c)
elif b>=c>=a:
    print(a)
elif c>=a>=b:
    print(b)
elif c>=b>=a:
    print(a)
elif a>=b>=c:
    print(c)
else:
    print(b)
