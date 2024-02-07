from math import gcd
def lcm(x,y):
    return int((x*y)/gcd(x,y))

print(f'{lcm(12,18)}')