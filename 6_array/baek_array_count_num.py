# 백준 2577번
# 결과값을 반복문 돌린다. 0~9까지 i와 같은 것의 갯수구함
a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c))
for i in range(10):
    count = 0
    for j in result:
        if i == int(j):
            count += 1
    print(count)