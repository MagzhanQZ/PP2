a = int(input())
sum = 0
while a != 0:
    b = int(input())
    if b != 0 and a < b:
        sum += 1
    a = b
print(sum)