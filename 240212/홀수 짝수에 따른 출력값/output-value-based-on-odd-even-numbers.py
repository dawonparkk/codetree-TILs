# def num(n):
#     add = 0
#     if n%2==1:
#         for i in range(1,n+1,2):
#             add+=i
#         return add
#     else:
#         for i in range(2,n+1,2):
#             add+=i
#         return add

# n = int(input())
# print(num(n))


# n = int(input())
 
#############################################

# 1부터 n까지의 n과 홀짝이 같은 수들의 합을 반환합니다.
def get_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # n과 홀짝이 같은 수만을 재귀함수로 호출합니다.
    return get_num(n - 2) + n


print(get_num(n))