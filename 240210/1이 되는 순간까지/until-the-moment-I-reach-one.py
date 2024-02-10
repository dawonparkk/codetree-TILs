def count(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0: 
        n=n//2
        cnt = cnt+1
        return count(n) 
    else:
        n=n//3
        cnt = cnt+1
        return count(n) 
cnt = 0
n=int(input())
print(count(n))