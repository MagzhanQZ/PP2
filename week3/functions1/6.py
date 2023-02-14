s = [str(x) for x in input().split()]
def rev(s):
    i = len(s) - 1
    while i >= 0:
        print(s[i], end=' ')
        i -= 1

rev(s)