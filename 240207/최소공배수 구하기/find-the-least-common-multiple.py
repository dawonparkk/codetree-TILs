from math import gcd
x,y = input().split()
x = int(x)
y = int(y)
print(f'{int((x*y)/gcd(x,y))}')