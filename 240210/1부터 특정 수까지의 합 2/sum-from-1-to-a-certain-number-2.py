def num(n):
    if n == 1:
        return 1
    return num(n-1)+n

n = int(input())
print(num(n))