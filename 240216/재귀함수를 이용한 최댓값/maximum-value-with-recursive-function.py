n = int(input())
arr = list(map(int, input().split()))
x = -1
def f(n):
    if n==0:
        return max(arr[0], x)
    return max(f(n-1), arr[n])
print(f(n-1))