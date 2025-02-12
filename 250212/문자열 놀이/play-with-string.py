operations, num = input().split()
num = int(num)
s = list(operations)
list_a = []
for i in range(num):
    list_a.append(input())

for op in list_a:
    op = op.split()
    if op[0] == '1': 
        a, b = int(op[1]) - 1, int(op[2]) - 1
        s[a], s[b] = s[b], s[a]
    elif op[0] == '2':  
        s = [op[2] if char == op[1] else char for char in s]
    print(''.join(s))