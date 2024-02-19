n = int(input())
arr = list(map(int, input().split()))

def f(a):
    if a==0 :
        return(arr[a])
    return(max(f(a-1),arr[a]))

print(f(n-1))