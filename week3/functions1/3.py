def solve(numheads, numlegs):
    x = ((2 * numheads) - numlegs ) / - 2
    y = numheads - x
    return x,y

print(solve(35, 94))