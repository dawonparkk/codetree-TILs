def num(n):
    if n < 10 :
        return (n%10)**2
    return num(n//10)+(n%10)**2
n = int(input())
print(num(n))

# 36 25 16 9 4 1

# 30 25 36