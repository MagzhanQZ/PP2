s = [int(a) for a in input().split()]


def Unique(s):
    list = []
    for a in s:
        if a not in list:
            list.append(a)
    print(list)


cn = Unique(s)