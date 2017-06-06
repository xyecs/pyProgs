from fractions import gcd
from functools import reduce

def lcm(a,b):
    lcm = (a*b) / gcd(a,b)
    return lcm 

print reduce(lcm, range(1,21))