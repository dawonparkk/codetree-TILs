def num(n):
    add = 0
    if n%2==1:
        for i in range(1,n+1,2):
            add+=i
        return add
    else:
        for i in range(2,n+1,2):
            add+=i
        return add

n = int(input())
print(num(n))