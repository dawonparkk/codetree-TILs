n,m = input().split()
n = int(n)
m = int(m)
arr = [[ 0 for _ in range(m)] for _ in range(n)]

num=1
for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num+=1 
for row in arr:
    print(" ".join(map(str,row)))