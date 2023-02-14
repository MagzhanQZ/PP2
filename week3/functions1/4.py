def isprime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def filterprime(list):
    new_list=[]
    for i in list:
        if isprime(i):
            new_list.append(i)
    return new_list
print(filterprime([1, 3, 5, 6]))