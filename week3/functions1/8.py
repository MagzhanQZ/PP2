list=[int(m) for m in input().split()]
def spy_game(list):
    l = []
    for a in list:
        if a == 0 or a == 7:
            l.append(a)
    if l[0] == 0 and l[1] == 0 and l[2] == 7:
        print(True)
    else:
        print(False)

c = spy_game(list)