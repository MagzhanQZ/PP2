from itertools import permutations
def permut(str):
    return [" ".join(x) for x in permutations(str)]
permut("Magzhan")
