a,b,c =  list(map(int, input().split()))

def add(n):
    if n < 10:
        return n
    return add(n//10)+(n%10)
print(add(a*b*c))