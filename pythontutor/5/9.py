max = 0
a = -1
b = -1
len = 0
while b != 0:
    b = int(input())
    if b > max:
        max = b
        a = len
    len += 1
print(a)